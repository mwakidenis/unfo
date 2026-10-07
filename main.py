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
import sys
import requests

def get_github_data(url, headers):
    results = []
    while url:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        results.extend(response.json())

        # GitHub paginates responses with 'Link' headers. Find the 'next' page URL if it exists.
        if 'next' in response.links:
            url = response.links['next']['url']
        else:
            url = None
    return results

try:
    token = sys.argv[1] if sys.argv else None
except (KeyError, IndexError):
    token = None

headers = {"Authorization": f"token {token}"}

# Get list of users you follow
following_url = "https://api.github.com/user/following"
following = [user['login'] for user in get_github_data(following_url, headers)]

# Get list of your followers
followers_url = "https://api.github.com/user/followers"
followers = [user['login'] for user in get_github_data(followers_url, headers)]

non_followers = []
for i_follow in following:
    if i_follow not in followers:
        non_followers.append(i_follow)

for user in non_followers:
    unfollow_url = f"https://api.github.com/user/following/{user}"
    unfollow_response = requests.delete(unfollow_url, headers=headers)
    if unfollow_response.status_code == 204:
        print(f"Unfollowed {user}")
    else:
        print(f"Failed to unfollow {user}: {unfollow_response.status_code}")
