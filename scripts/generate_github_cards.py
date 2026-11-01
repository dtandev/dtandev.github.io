#!/usr/bin/env python3
"""Generate static GitHub stats / top-languages SVG cards for the homepage.

Replaces the previously embedded github-readme-stats.vercel.app images (a shared
free demo deployment that gets paused/rate-limited) with cards rendered from the
GitHub REST/GraphQL APIs and committed straight into the repo.

Requires a GITHUB_TOKEN with public read access (the default Actions token works).
"""

import json
import os
import sys
import urllib.error
import urllib.request

USERNAME = "dtandev"
EXCLUDE_LANGS = {"html", "just"}
LANG_COLORS = {
    "python": "#3572A5",
    "jupyter notebook": "#DA5B0B",
    "javascript": "#f1e05a",
    "typescript": "#3178c6",
    "html": "#e34c26",
    "css": "#563d7c",
    "shell": "#89e051",
    "plpgsql": "#336790",
    "go": "#00ADD8",
    "rust": "#dea584",
    "java": "#b07219",
    "c++": "#f34b7d",
    "c": "#555555",
    "dockerfile": "#384d54",
    "makefile": "#427819",
    "vue": "#41b883",
    "r": "#198CE7",
    "julia": "#a270ba",
    "matlab": "#e16737",
}
DEFAULT_LANG_COLOR = "#8a8a8a"

THEMES = {
    "light": {"title": "#3b2313", "text": "#5c4033", "icon": "#d97706"},
    "dark": {"title": "#d49255", "text": "#e0cab6", "icon": "#d49255"},
}

API = "https://api.github.com"


def gh_get(path, token):
    req = urllib.request.Request(
        f"{API}{path}",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "dtandev-github-cards",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def gh_graphql(query, variables, token):
    req = urllib.request.Request(
        f"{API}/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "dtandev-github-cards",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def fetch_repos(token):
    repos, page = [], 1
    while True:
        batch = gh_get(f"/users/{USERNAME}/repos?type=owner&per_page=100&page={page}", token)
        if not batch:
            break
        repos.extend(batch)
        page += 1
    return repos


def total_stars(repos):
    return sum(r["stargazers_count"] for r in repos)


def total_prs(token):
    data = gh_get(f"/search/issues?q=author:{USERNAME}+type:pr", token)
    return data.get("total_count", 0)


def total_commits(token):
    created_at = gh_get(f"/users/{USERNAME}", token)["created_at"]
    start_year = int(created_at[:4])
    import datetime

    current_year = datetime.datetime.now(datetime.timezone.utc).year
    query = """
    query($login: String!, $from: DateTime!, $to: DateTime!) {
      user(login: $login) {
        contributionsCollection(from: $from, to: $to) {
          totalCommitContributions
          restrictedContributionsCount
        }
      }
    }
    """
    total = 0
    for year in range(start_year, current_year + 1):
        variables = {
            "login": USERNAME,
            "from": f"{year}-01-01T00:00:00Z",
            "to": f"{year}-12-31T23:59:59Z",
        }
        result = gh_graphql(query, variables, token)
        coll = result["data"]["user"]["contributionsCollection"]
        total += coll["totalCommitContributions"] + coll["restrictedContributionsCount"]
    return total


def language_breakdown(repos, token):
    totals = {}
    for repo in repos:
        if repo["fork"]:
            continue
        langs = gh_get(f"/repos/{USERNAME}/{repo['name']}/languages", token)
        for lang, byte_count in langs.items():
            if lang.lower() in EXCLUDE_LANGS:
                continue
            totals[lang] = totals.get(lang, 0) + byte_count
    grand_total = sum(totals.values()) or 1
    ranked = sorted(totals.items(), key=lambda kv: -kv[1])[:5]
    return [(lang, byte_count / grand_total) for lang, byte_count in ranked]


def render_stats_card(theme_name, stats):
    c = THEMES[theme_name]
    rows = [
        ("★", "Total Stars Earned", f"{stats['stars']:,}"),
        ("\U0001F501", "Total Commits", f"{stats['commits']:,}"),
        ("⎇", "Total Pull Requests", f"{stats['prs']:,}"),
    ]
    row_height = 34
    height = 56 + row_height * len(rows)
    width = 320

    rows_svg = []
    for i, (icon, label, value) in enumerate(rows):
        y = 56 + i * row_height
        rows_svg.append(
            f'<text x="25" y="{y}" font-size="15" fill="{c["icon"]}">{icon}</text>'
            f'<text x="50" y="{y}" font-size="14" fill="{c["text"]}">{label}</text>'
            f'<text x="{width - 25}" y="{y}" font-size="14" fill="{c["text"]}" '
            f'text-anchor="end" font-weight="600">{value}</text>'
        )

    return f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif">
  <text x="25" y="28" font-size="17" font-weight="700" fill="{c["title"]}">{USERNAME}&#8217;s GitHub Stats</text>
  {''.join(rows_svg)}
</svg>'''


def render_langs_card(theme_name, langs):
    c = THEMES[theme_name]
    row_height = 28
    height = 56 + row_height * len(langs)
    width = 320
    bar_width = width - 50

    bar_segments = []
    x = 25
    for lang, frac in langs:
        color = LANG_COLORS.get(lang.lower(), DEFAULT_LANG_COLOR)
        seg_width = max(frac * bar_width, 2)
        bar_segments.append(f'<rect x="{x:.1f}" y="40" width="{seg_width:.1f}" height="8" rx="4" fill="{color}"/>')
        x += seg_width

    rows_svg = []
    for i, (lang, frac) in enumerate(langs):
        color = LANG_COLORS.get(lang.lower(), DEFAULT_LANG_COLOR)
        y = 70 + i * row_height
        pct = f"{frac * 100:.1f}%"
        rows_svg.append(
            f'<circle cx="30" cy="{y - 5}" r="5" fill="{color}"/>'
            f'<text x="44" y="{y}" font-size="13" fill="{c["text"]}">{lang}</text>'
            f'<text x="{width - 25}" y="{y}" font-size="13" fill="{c["text"]}" '
            f'text-anchor="end">{pct}</text>'
        )

    return f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif">
  <text x="25" y="28" font-size="17" font-weight="700" fill="{c["title"]}">Most Used Languages</text>
  {''.join(bar_segments)}
  {''.join(rows_svg)}
</svg>'''


def main():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN environment variable is required", file=sys.stderr)
        sys.exit(1)

    out_dir = os.path.join(os.path.dirname(__file__), "..", "static", "media", "github")
    os.makedirs(out_dir, exist_ok=True)

    try:
        repos = fetch_repos(token)
        stats = {
            "stars": total_stars(repos),
            "prs": total_prs(token),
            "commits": total_commits(token),
        }
        langs = language_breakdown(repos, token)
    except urllib.error.HTTPError as e:
        print(f"GitHub API error: {e.code} {e.reason}: {e.read().decode()}", file=sys.stderr)
        sys.exit(1)

    for theme in THEMES:
        with open(os.path.join(out_dir, f"stats-{theme}.svg"), "w") as f:
            f.write(render_stats_card(theme, stats))
        with open(os.path.join(out_dir, f"langs-{theme}.svg"), "w") as f:
            f.write(render_langs_card(theme, langs))

    print("Stats:", stats)
    print("Languages:", langs)


if __name__ == "__main__":
    main()
