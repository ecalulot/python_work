nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https'))
print(nostarch_url.removeprefix('https://'))
new_url = nostarch_url.removeprefix('https:/')
print(new_url)
