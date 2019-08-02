class Website:
    host = None
    domain = None
    queries = None

    def __init__(self, host, domain, queries):
        self.host = host
        self.domain = domain
        self.queries = queries


input_row = input()
websites = []

while input_row != "end":
    data = input_row.split(' | ')
    host = data[0]
    domain = data[1]
    queries = ''

    if len(data) > 2:
        queries = data[2].split(',')

    website = Website(host, domain, queries)
    websites.append(website)

    input_row = input()


for website in websites:
    if website.queries:
        print(f"https://www.{website.host}.{website.domain}/query?=", end='')

        if website.queries:
            for i in range(0, len(website.queries)):
                if i != len(website.queries)-1:
                    print(f"[{website.queries[i]}]&", end='')
                else:
                    print(f"[{website.queries[i]}]", end='')
            print()
    else:
        print(f"https://www.{website.host}.{website.domain}", end='')
