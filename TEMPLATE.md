# README ABOUT ME #

![Hello](images/general/hello.gif)

Hello, <img src="images/general/hi.gif" width="32px" height="32px"> my name is {{name}}.

This is my Official GitHub Account.

## Projects ##
{% if projects is defined and projects %}
{% for group in projects %}
### {{group.name}} ###
{% if group.projects is defined and group.projects %}
| Project name | License | Technoloy | Description |
| ------------ | ------- | --------- | ----------- |
{% for project in group.projects %}| [{{project.name}}]({{project.link}}) | {% for license in project.licenses %}![{{license}}](images/licenses/{{license}}.svg) {% endfor %} | {% for technology in project.technologies %}![{{technology}}](images/tech/{{technology}}.svg) {% endfor %} | {{project.description}} | 
{% endfor %}
{% else %}
No projects yet. I said **"not yet."**
{% endif %}
{% endfor %}
{% endif %}

## Social ##

{% if links is defined and links %}{% for link in links %} <a href="{{link.link}}"><img src="images/social/{{link.name}}.svg" width="64px" height="64px" alt="{{link.name}}"></a> {% endfor %}{% else %}No links yet. I said "not yet."{% endif %}

## LeetCode ##

[![LeetCode user Alimektor](https://img.shields.io/badge/dynamic/json?style=for-the-badge&labelColor=black&color=%23ffa116&label=Ranking&query=ranking&url=https%3A%2F%2Fleetcode-badge.vercel.app%2Fapi%2Fusers%2FAlimektor&logo=leetcode&logoColor=yellow)](https://leetcode.com/Alimektor/)

[![LeetCode user Alimektor](https://img.shields.io/badge/dynamic/json?style=for-the-badge&labelColor=black&color=%23ffa116&label=Solved&query=solvedOverTotal&url=https%3A%2F%2Fleetcode-badge.vercel.app%2Fapi%2Fusers%2FAlimektor&logo=leetcode&logoColor=yellow)](https://leetcode.com/Alimektor/)

[![LeetCode user Alimektor](https://img.shields.io/badge/dynamic/json?style=for-the-badge&labelColor=black&color=%23ffa116&label=Solved&query=solvedPercentage&url=https%3A%2F%2Fleetcode-badge.vercel.app%2Fapi%2Fusers%2FAlimektor&logo=leetcode&logoColor=yellow)](https://leetcode.com/Alimektor/)

## Codewars ##

<a href="https://www.codewars.com/users/Alimektor"><img src="https://www.codewars.com/users/Alimektor/badges/large" alt="Codewars"></a>

## Duolingo ## 

<a href="https://www.duolingo.com/profile/Alimektor"><img src="https://duolingo-stats-card.vercel.app/api?username=Alimektor&theme=purple-gang" alt="Duolingo"></a>

## Others ##

[![Valorant Badge](https://img.shields.io/badge/Valorant-FA4454?logo=valorant&logoColor=fff&style=flat-square)](https://tracker.gg/valorant/profile/riot/%E3%82%A2%E3%83%AA%E3%83%A1%E3%82%AF%E3%82%BF%E3%83%BC%23%E3%82%A2%E3%83%AC%E3%83%8D%E3%82%AF%E3%83%88/overview)

----

![Dino](images/general/dino.gif)

Last Updated: {{last_updated}}
