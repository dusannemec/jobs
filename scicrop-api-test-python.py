import requests

from datetime import datetime

def main():

	URL_API = 'https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume'

	resume = {
		"full_name": "Rodrigo Souza Lins",
		"email": "rodrigolins@protonmail.com",
		"mobile_phone": "+55 (11) 98933-1591",
		"age": 18,
		"home_address": "Rua do Controle 67, Vila Bancária",
		"start_date": int(datetime.timestamp(datetime.now())),
		"opportunity_tag": "dev_intern_200",
		"past_jobs_experience": "I worked as designer at Lufran Artefatos de Cimento",
		"degrees": [{
			"institution_name": "Universidade São Judas Tadeu",
			"degree_name": "Ciência da Computação",
			"begin_date": int(datetime.timestamp(datetime(2019, 2, 19))),
			"end_date": int(datetime.timestamp(datetime(2022, 11, 30)))
		}],
		"programming_skills": ["python", "java"],
		"database_skills": ["mysql"],
		"hobbies": ["read", "videogames", "series"],
		"why": "I'm looking for somewhere to start my developer career. I want to learn everything I can and do my best.",
		"git_url_repositories": "https://github.com/dusannemec"
	}

	response = requests.post(url=URL_API, json=resume)
	print(response.status_code)

if __name__ == '__main__':
	main()
