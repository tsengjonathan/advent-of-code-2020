from collections import defaultdict


def parse_upstream_relationships(filename):
    relationships = defaultdict(list)
    with open(filename, 'r') as f:
        for line in f:
            line = line[:-2]

            if 'no other bags' in line:
                continue

            tokens = line.split()
            parent_bag = ' '.join(tokens[:2])

            children_bags = ' '.join(tokens[4:]).split(', ')
            for children_bag in children_bags:
                children_bag_tokens = children_bag.split(' ')
                bag_color = ' '.join(children_bag_tokens[1:3])
                relationships[bag_color].append(parent_bag)
    return dict(relationships)


def calculate_valid_parents(relationships):
    bag = 'shiny gold'
    stack = [bag]
    parents = set()

    while stack:
        parent = stack.pop()
        parents.add(parent)

        for grandparent in relationships.get(parent, []):
            stack.append(grandparent)

    parents.remove(bag)
    return parents


def parse_downstream_relationships(filename):
    relationships = defaultdict(list)
    with open(filename, 'r') as f:
        for line in f:
            line = line[:-2]

            tokens = line.split()
            parent_bag = ' '.join(tokens[:2])

            if 'no other bags' in line:
                # relationships[parent_bag].append((0, None))
                continue

            assert len(relationships[parent_bag]) == 0

            children_bags = ' '.join(tokens[4:]).split(', ')
            for children_bag in children_bags:
                children_bag_tokens = children_bag.split(' ')
                count = int(children_bag_tokens[0])
                bag_color = ' '.join(children_bag_tokens[1:3])
                relationships[parent_bag].append((count, bag_color))

    return dict(relationships)


def count_total_bags_helper(relationships, bag):
    count = 1

    if bag not in relationships:
        return count

    for child_bag in relationships[bag]:
        count += child_bag[0] * \
            count_total_bags_helper(relationships, child_bag[1])

    return count


def count_total_bags(relationships):
    bag = 'shiny gold'
    return count_total_bags_helper(relationships, bag) - 1


if __name__ == "__main__":
    filename = 'input.txt'
    up_relationships = parse_upstream_relationships(filename)
    valid_parents = calculate_valid_parents(up_relationships)
    print(f'Part One Answer: {len(valid_parents)}')
    down_relationships = parse_downstream_relationships(filename)
    total_child_bags = count_total_bags(down_relationships)
    print(f'Part Two Answer: {total_child_bags}')
