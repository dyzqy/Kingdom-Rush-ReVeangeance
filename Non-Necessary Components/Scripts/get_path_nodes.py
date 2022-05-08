import pickle

DIRECTORY = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Kingdom Rush Vengeance\\'

def get_nodes(directory, level):
    paths = []
    subpaths = []
    nodes = []
    coords = []
    active = False

    with open(directory + f'KR4\\Level\\level{level}_data.plist', 'r') as file:
        prev_line = ''
        for i, line in enumerate(file):
            if active and line.strip() == '</array>' and line.find('<') == 1:
                paths.append(subpaths.copy())
                break
            
            line = line.strip()

            if line == '<key>paths_pc</key>':
                active = True

            elif not active:
                continue

            elif line == '<key>subpaths</key>' and subpaths != []:
                paths.append(subpaths.copy())
                subpaths = []

            elif line == '</array>':
                subpaths.append(nodes.copy())
                nodes = []

            elif prev_line == '<key>x</key>':
                coords.append(float(line.replace('<string>', '').replace('</string>', '')))

            elif prev_line == '<key>y</key>':
                coords.append(float(line.replace('<string>', '').replace('</string>', '')))
                nodes.append(coords.copy())
                coords = []

            prev_line = line

    pickle.dump(paths, open(directory + f'Revengeance\\Nodes\\level{level}_nodes', 'wb'))

for i in range(29):
    if i not in [23, 24, 25]:
        get_nodes(DIRECTORY, i)
