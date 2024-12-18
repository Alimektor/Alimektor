# README ABOUT ME #

![Hello](images/general/hello.gif)

Hello, <img src="images/general/hi.gif" width="32px" height="32px"> my name is {{name}}.

This is my Official GitHub Account.

## Projects ##
{% if public_projects is defined and public_projects %}{% for project in public_projects %}
- [{{project.name}}](https://github.com/{{project.owner.login}}/{{project.name}}) ![{{project.name}} License](https://img.shields.io/github/license/{{project.owner.login}}/{{project.name}}.svg?style=plastic) ![{{project.name}} Language](https://img.shields.io/github/languages/top/{{project.owner.login}}/{{project.name}}.svg?style=plastic) ![{{project.name}} Language](https://img.shields.io/github/stars/{{project.owner.login}}/{{project.name}}.svg?style=plastic) — {{project.description}}{% endfor %}
{% endif %}
{% if archive_projects is defined and archive_projects %}<details>
<summary>Archive Projects</summary>
{% for project in archive_projects %}
- [{{project.name}}](https://github.com/{{project.owner.login}}/{{project.name}}) ![{{project.name}} License](https://img.shields.io/github/license/{{project.owner.login}}/{{project.name}}.svg?style=plastic) ![{{project.name}} Language](https://img.shields.io/github/languages/top/{{project.owner.login}}/{{project.name}}.svg?style=plastic) ![{{project.name}} Language](https://img.shields.io/github/stars/{{project.owner.login}}/{{project.name}}.svg?style=plastic) — {{project.description}}
{% endfor %}</details>
{% endif %}

## Social ##

{% if links is defined and links %}{% for link in links %}[![{{link.name}}](https://img.shields.io/badge/{{link.badge}})]({{link.url}}){% endfor %}{% else %}No links yet. I said "not yet."{% endif %}

## Learning ##

> Practice makes perfect.

I am actively learning on various platforms and solving programming problems. Here are some statistics of my learning progress:

<details>

<summary>LeetCode</summary>

I like LeetCode. I don't have time to go through it that often at the moment, but it keeps me going.

[![LeetCode user Alimektor](https://img.shields.io/badge/dynamic/json?style=for-the-badge&labelColor=black&color=%23ffa116&label=Ranking&query=ranking&url=https%3A%2F%2Fleetcode-badge.vercel.app%2Fapi%2Fusers%2FAlimektor&logo=leetcode&logoColor=yellow)](https://leetcode.com/Alimektor/)

[![LeetCode user Alimektor](https://img.shields.io/badge/dynamic/json?style=for-the-badge&labelColor=black&color=%23ffa116&label=Solved&query=solvedOverTotal&url=https%3A%2F%2Fleetcode-badge.vercel.app%2Fapi%2Fusers%2FAlimektor&logo=leetcode&logoColor=yellow)](https://leetcode.com/Alimektor/)

[![LeetCode user Alimektor](https://img.shields.io/badge/dynamic/json?style=for-the-badge&labelColor=black&color=%23ffa116&label=Solved&query=solvedPercentage&url=https%3A%2F%2Fleetcode-badge.vercel.app%2Fapi%2Fusers%2FAlimektor&logo=leetcode&logoColor=yellow)](https://leetcode.com/Alimektor/)

</details>

<details>

<summary>Codewars</summary>

Codewars is a platform where you can learn some syntactic sugar for a certain. I usually use it to quickly learn the basics of some language with examples.

<a href="https://www.codewars.com/users/Alimektor"><img src="https://www.codewars.com/users/Alimektor/badges/large" alt="Codewars"></a>

</details>

<details>

<summary>Duolingo</summary>

Most likely, this app is just good practice for a taxi ride. But friends are on the app and a little practice is good. Plus it disciplines me to build useful habits.

<a href="https://www.duolingo.com/profile/Alimektor"><img src="https://duolingo-stats-card.vercel.app/api?username=Alimektor&theme=purple-gang" alt="Duolingo"></a>

</details>

## Gaming ##

I'm the kind of gamer who loves many genres. You can always discuss any existing game with me. Check out what I'm [playing right now](https://www.igdb.com/users/alimektor/lists/playing) or what I've already [played](https://www.igdb.com/users/alimektor/lists/played).

<details>

<summary>Valorant</summary>

Yeah, I'm playing Valorant. Just not alone.

[![Valorant Badge](https://img.shields.io/badge/Valorant-FA4454?logo=valorant&logoColor=fff&style=flat-square)](https://tracker.gg/valorant/profile/riot/%E3%82%A2%E3%83%AA%E3%83%A1%E3%82%AF%E3%82%BF%23%E3%82%A2%E3%83%AC%E3%83%8D%E3%82%AF%E3%83%88/overview)

</details>

----

![Dino](images/general/dino.gif)

Last Updated: {{last_updated}}
