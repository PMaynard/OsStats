# Folding Stats

Datasources from:
- http://fah-web.stanford.edu/daily_user_summary.txt.bz2
- http://fah-web.stanford.edu/daily_team_summary.txt.bz2 

Cron retrieval once per hour: 

	0 * * * * curl http://fah-web.stanford.edu/daily_team_summary.txt.bz2 -o "$(date +\%d-\%m-\%y-\%H-\%M)-team.txt.bz2" > /dev/null
	0 * * * * curl http://fah-web.stanford.edu/daily_user_summary.txt.bz2 -o "$(date +\%d-\%m-\%y-\%H-\%M)-user.txt.bz2" > /dev/null


Get the difference: 
	
	diff daily_team_summary.txt 16-08-15-03-22-team.txt | grep '>' | cut -c 3- > diff.text
	diff daily_team_summary.txt 16-08-15-03-22-team.txt --unchanged-line-format="" --old-line-format="" --new-line-format="%dn     %L"