<a><img src='https://i.imgur.com/LyHic3i.gif'/></a>
<h1 align="center"> 𝐔𝐍𝐅𝐎𝐋𝐋𝐎𝐖𝐄𝐑 </h1>

- **Be petty:** run a GitHub Actions workflow that automatically unfollows anyone in your following who doesn't follow you back.


<details>
<summary>NOTICE!!! (TAP TO READ)</summary>

- This runs entirely on **GitHub Actions** — no server, no VPS, no hosting costs.
- You **must fork this repo** — the workflow will not run on the original.
- The unfollow action is **permanent**. GitHub does not have an undo for unfollows.
- Scheduled workflows are **disabled after 60 days of repo inactivity**. Push any commit or run it manually to keep it alive.

</details>

<a><img src='https://i.imgur.com/LyHic3i.gif'/></a>

  <p align="center">
<a href="https://github.com/mwakidenis"><img title="GITHUB" src="https://img.shields.io/badge/GITHUB-MWAKIDENIS-red.svg?style=for-the-badge&logo=github"></a>
<p/>
<p align="center">
<a href="https://github.com/mwakidenis?tab=followers"><img title="Followers" src="https://img.shields.io/github/followers/mwakidenis?label=Followers&style=social"></a>
<a href="https://github.com/mwakidenis/unfollower/stargazers/"><img title="STARS" src="https://img.shields.io/github/stars/mwakidenis/unfollower?&style=social"></a>
<a href="https://github.com/mwakidenis/unfollower/network/members"><img title="Forks" src="https://img.shields.io/github/forks/mwakidenis/unfollower?style=social"></a>
<a href="https://github.com/mwakidenis/unfollower/watchers"><img title="Watching" src="https://img.shields.io/github/watchers/mwakidenis/unfollower?label=Watching&style=social"></a>

<a><img src='https://i.imgur.com/LyHic3i.gif'/></a>

## 𝟏. 𝐅𝐎𝐑𝐊 𝐑𝐄𝐏𝐎 (𝐀 𝐌𝐔𝐒𝐓):

**👇FORK REPO**
<details>
<summary>𝗖𝗟𝗜𝗖𝗞 𝗛𝗘𝗥𝗘</summary>
  
- This is essential — GitHub Actions only run on **your own** fork, not on this repo.

<a href="https://github.com/mwakidenis/unfollower/fork"><img src="https://img.shields.io/badge/CLICK%20HERE-purple" alt="FORK" width="150"></a>
</details>

<a><img src='https://i.imgur.com/LyHic3i.gif'/></a>

### 𝟐. 𝐄𝐍𝐀𝐁𝐋𝐄 𝐀𝐂𝐓𝐈𝐎𝐍𝐒

<details>
<summary>TAP TO OPEN</summary>

Go to your forked repository and enable workflows:

- `Settings` -> `Actions` -> `General`
- Select **Allow all actions and reusable workflows**
- Click **Save**

</details>

<a><img src='https://i.imgur.com/LyHic3i.gif'/></a>

### 𝟑. 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄 𝐏𝐄𝐑𝐒𝐎𝐍𝐀𝐋 𝐀𝐂𝐂𝐄𝐒𝐒 𝐓𝐎𝐊𝐄𝐍:

<details>
<summary>GET YOUR PAT</summary>
<a href="https://github.com/settings/tokens"><img src="https://img.shields.io/badge/CLICK%20HERE-green" alt="Generate Token" width="150"></a>

- Click **Generate new token** -> **Generate new token (classic)**
- Under the `user` scope, tick the **`user:follow`** sub-scope
- Copy the token immediately — GitHub only shows it once
</details>

<a><img src='https://i.imgur.com/LyHic3i.gif'/></a>

### 𝟒. 𝐀𝐃𝐃 𝐓𝐇𝐄 𝐒𝐄𝐂𝐑𝐄𝐓:

<details>
<summary>TAP TO OPEN</summary>

In your forked repository:

1. Go to `Settings`
2. Go to `Secrets and variables` -> `Actions`
3. Click **New repository secret**
4. Name it exactly: **`GH_TOKEN`**
5. Paste your Personal Access Token as the value
6. Click **Add secret**

> Without `GH_TOKEN` the workflow will fail on the unfollow step.
</details>

<a><img src='https://i.imgur.com/LyHic3i.gif'/></a>

### 𝟓. 𝐒𝐂𝐇𝐄𝐃𝐔𝐋𝐄 𝐂𝐎𝐍𝐅𝐈𝐆:

The repository currently runs **every 5 days**, and can be changed in the `unfollow.yml` file under the `.github/workflows` directory using cron logic.

The current cron schedule is set to run every 3 hours. The schedule can be updated in the workflow yml:
<a><img src='https://i.imgur.com/LyHic3i.gif'/></a>

### 6. 𝐋𝐈𝐂𝐄𝐍𝐒𝐄 𝐇𝐄𝐀𝐃𝐄𝐑 𝐅𝐎𝐑 𝐒𝐎𝐔𝐑𝐂𝐄 𝐅𝐈𝐋𝐄𝐒

<details>
<summary>𝗧𝗔𝗣 𝗧𝗢 𝗩𝗜𝗘𝗪</summary>

GPL v2.0 recommends putting a short copyright notice at the **top of every source file**. Add this to the top of `main.py` (and any other `.py` file):

```python
# Unfollower - GitHub Actions auto-unfollow tool
# Copyright (C) 2026  mwakidenis
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
