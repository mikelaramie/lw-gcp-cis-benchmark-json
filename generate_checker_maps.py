import json
import subprocess

result = subprocess.run(["lacework", "api", "get", "/api/v1/external/recommendations/azure"], stdout=subprocess.PIPE)
checkers = json.loads(result.stdout.decode("utf-8"))['data'][0]

with open('checkers.json', 'w') as outfile:
    json.dump(checkers, outfile)
#
# f = open('checkers.json', )
# checkers = json.load(f)

checkers_131 = [checker for checker in checkers if ("131" in checker)]
checkers_10 = [checker for checker in checkers if ("131" not in checker)]

checkers_131.sort()
checkers_10.sort()

disable_map_10 = {}
enable_map_10 = {}
for checker in checkers_10:
    disable_map_10[checker] = 'disable'
    enable_map_10[checker] = 'enable'

disable_map_131 = {}
enable_map_131 = {}
for checker in checkers_131:
    disable_map_131[checker] = 'disable'
    enable_map_131[checker] = 'enable'

print("updated disable_map_10 added to disable_cis_10.json")
with open('disable_cis_10.json', 'w') as outfile:
    json.dump(disable_map_10, outfile, indent=4)
    outfile.write('\n\n\n')
    outfile.write('//Single line for Copy/Paste\n')
    json.dump(disable_map_10, outfile)
    outfile.write('\n')

print("updated enable_map_10 added to enable_cis_10.json")
with open('enable_cis_10.json', 'w') as outfile:
    json.dump(enable_map_10, outfile, indent=4)
    outfile.write('\n\n\n')
    outfile.write('//Single line for Copy/Paste\n')
    json.dump(enable_map_10, outfile)
    outfile.write('\n')

print("updated disable_map_131 added to disable_cis_131.json")
with open('disable_cis_131.json', 'w') as outfile:
    json.dump(disable_map_131, outfile, indent=4)
    outfile.write('\n\n\n')
    outfile.write('//Single line for Copy/Paste\n')
    json.dump(disable_map_131, outfile)
    outfile.write('\n')

print("updated enable_map_131 added to enable_cis_131.json")
with open('enable_cis_131.json', 'w') as outfile:
    json.dump(enable_map_131, outfile, indent=4)
    outfile.write('\n\n\n')
    outfile.write('//Single line for Copy/Paste\n')
    json.dump(enable_map_131, outfile)
    outfile.write('\n')
