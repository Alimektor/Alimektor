# README ABOUT ME #

![Hello](images/general/hello.gif)

Hello, <img src="images/general/hi.gif" width="32px" height="32px"> my name is {{name}}.

This is my Official GitHub Account.

## Projects ##
{% if projects is defined and projects %}
{% for group in projects %}
### {{group.name}} ###
{% if group.projects is defined and group.projects %}
{% for project in group.projects %}
- [{{project.name}}]({{project.link}}) {% for license in project.licenses %}![{{license}}](images/licenses/{{license}}.svg) {% endfor %} {% for technology in project.technologies %}![{{technology}}](images/tech/{{technology}}.svg) {% endfor %} — {{project.description}}
{% endfor %} 
{% else %}
No projects yet. I said **"not yet."**
{% endif %}
{% endfor %}
{% endif %}

## Social ##

{% if links is defined and links %}{% for link in links %} <a href="{{link.link}}"><img src="images/social/{{link.name}}.svg" width="64px" height="64px" alt="{{link.name}}"></a> {% endfor %}{% else %}No links yet. I said "not yet."{% endif %}

## Codewars ##

<a href="https://www.codewars.com/users/Alimektor"><img src="https://www.codewars.com/users/Alimektor/badges/large" alt="Codewars"></a>

![Dino](images/general/dino.gif)

Last Updated: {{last_updated}}
