
url = input("URL: ")

if "https" in url:
    url_type = url.split("https://")
    url = url_type[1]
    url_type = "HTTPS"
else:
    url_type = url.split("http://")
    url = url_type[1]
    url_type = "HTTP"

print(f"Protocol: {url_type}\n")


url_map = url.split("/")

variable_ar = []

if "?" in url_map[-1]:
    variables = url_map[-1].split("?")[1].split("&")
    for var in variables:
        split_tmp = var.split("=")
        variable_ar.append({'name': split_tmp[0], 'value': split_tmp[1]})
    url_map[-1] = url_map[-1].split("?")[0]

# mapping ⤷

counter = 0

for m in url_map:
    print(f"{counter * ' '} ⤷ {m}")
    counter = counter + 1

# Variables

print("\nVariables: \n")

for v in variable_ar:
    print(f"{v['name']} = {v['value']}")

