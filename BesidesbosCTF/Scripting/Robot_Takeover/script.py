import requests

URL = "http://challenge.ctf.games:30095/"

l_robots = "robots.txt"

flag = [""]*50
while 1:
	r = requests.get(url=URL+l_robots)

	robots_txt = r.text

	lst_robots_txt = robots_txt.split("\n")
	etat = True
	for i in lst_robots_txt:
		if not i == "":
			if i[0] == 'U':	# We define the user-agent to use
				headers = {"User-Agent": i[12:]}
			else:	# Then we do the GET request
				i = i[11:]
				r = requests.get(url=URL+i, headers=headers)
				resp = r.text
				if resp.startswith("REJOICE"):	# If the response begin with REJOICE we extract the 2 numbers
					number = []
					for words in resp.split():
						if words.isdigit():
							number.append(int(words))
					flag[number[0]] = i[number[1]]	# We fill the flag

		if len("".join(flag)) == 34:	# If the flag is complete (I knew that there was 34 characters with test at the begining)
			print("".join(flag))
			exit(1)