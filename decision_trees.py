import random
import math 
from collections import Counter ,defaultdict
from functools import partial


def entropy(class_probabilities):
	return sum(-p * math.log(p, 2) for p in class_probabilities if p > 0)
#print(entropy([1]))

def class_probabilities(labels):
    total_count = len(labels)
    return [count / total_count
            for count in Counter(labels).values()]
#print(class_probabilities([3,4,2,4]))

def data_entropy(labeled_data):
    labels = [label for _, label in labeled_data]
    probabilities = class_probabilities(labels)
    return entropy(probabilities)

def partition_entropy(subsets):
	total_count = sum(len(subset) for subset in subsets)
	return sum( data_entropy(subset) * len(subset) / total_count
		for subset in subsets )
inputs = [
    ({'level':'Senior', 'lang':'Java', 'tweets':'no', 'phd':'no'},    False),
    ({'level':'Senior', 'lang':'Java', 'tweets':'no', 'phd':'yes'},   False),
    ({'level':'Mid', 'lang':'Python', 'tweets':'no', 'phd':'no'},      True),
    ({'level':'Junior', 'lang':'Python', 'tweets':'no', 'phd':'no'},   True),
    ({'level':'Junior', 'lang':'R', 'tweets':'yes', 'phd':'no'},       True),
    ({'level':'Junior', 'lang':'R', 'tweets':'yes', 'phd':'yes'},     False),
    ({'level':'Mid', 'lang':'R', 'tweets':'yes', 'phd':'yes'},         True),
    ({'level':'Senior', 'lang':'Python', 'tweets':'no', 'phd':'no'},  False),
    ({'level':'Senior', 'lang':'R', 'tweets':'yes', 'phd':'no'},       True),
    ({'level':'Junior', 'lang':'Python', 'tweets':'yes', 'phd':'no'},  True),
    ({'level':'Senior', 'lang':'Python', 'tweets':'yes', 'phd':'yes'}, True),
    ({'level':'Mid', 'lang':'Python', 'tweets':'no', 'phd':'yes'},     True),
    ({'level':'Mid', 'lang':'Java', 'tweets':'yes', 'phd':'no'},       True),
    ({'level':'Junior', 'lang':'Python', 'tweets':'no', 'phd':'yes'}, False)
]
def partition_by(inputs, attribute):
	groups = defaultdict(list)
	for input_ in inputs:
		key = input_[0][attribute]   
		groups[key].append(input_)   
	return groups
print('parti:' ,partition_by(inputs,'lang'))

def partition_entropy_by(inputs, attribute):
	partitions = partition_by(inputs, attribute)
	print('r:' ,partitions)
	return partition_entropy(partitions.values())
for key in ['level','lang','tweets','phd']:
	print( key, partition_entropy_by(inputs, key))
#print(partition_entropy_by(inputs,'level'))

def build_tree_id3(inputs, split_candidates=None):
	if split_candidates is None:
		split_candidates = inputs[0][0].keys()
	num_inputs = len(inputs)
	num_trues = len([label for item, label in inputs if label])
	num_falses = num_inputs - num_trues
	if num_trues == 0: 
		return False
	if num_falses == 0: 
		return True 
	if not split_candidates:
		return num_trues >= num_falses 
	best_attribute = min(split_candidates,key=partial(partition_entropy_by, inputs))
	partitions = partition_by(inputs, best_attribute)

	new_candidates = [a for a in split_candidates
	if a != best_attribute]

	partitions = partition_by(inputs, best_attribute)
	subtrees = { attribute_value : build_tree_id3(subset, new_candidates)
	for attribute_value, subset in partitions.items() }
	
	subtrees[None] = num_trues > num_falses
	return (best_attribute, subtrees)
tree_1 = build_tree_id3(inputs[:5])
tree_2 = build_tree_id3(inputs[5:])
tree = build_tree_id3(inputs)

def classify(tree, input_):
	if tree in [True, False]:
		return tree
	attribute, subtree_dict = tree
	subtree_key = input_.get(attribute) 
	if subtree_key not in subtree_dict:
		subtree_key = None
	subtree = subtree_dict[subtree_key]
	return classify(subtree, input_) # choose the appropriate subtree

#print(classify(tree,{'level':'Senior', 'lang':'Python', 'tweets':'yes', 'phd':'no'}))

def forest_classify(trees, input):
	votes = [classify(tree, input) for tree in trees]
	vote_counts = Counter(votes)
	return vote_counts.most_common(1)[0][0]
trees = [tree_1,tree_2,tree]
#print(forest_classify(trees,{ "level" : "Junior",
#"lang" : "Java",
#"tweets" : "yes",
#"phd" : "no"}))

def build_tree_random(inputs,num_split_candidates, split_candidates=None):
 
	if split_candidates is None:
		split_candidates = inputs[0][0].keys()
	num_inputs = len(inputs)
	num_trues = len([label for item, label in inputs if label])
	num_falses = num_inputs - num_trues
	if num_trues == 0:
		return False
	if num_falses == 0:
		return True # no Trues? return a "False" leaf
	if not split_candidates:
		return num_trues >= num_falses # if no split candidates left
	if len(split_candidates) <= num_split_candidates:
		sampled_split_candidates = split_candidates
	else:
		sampled_split_candidates = random.sample(split_candidates,
								num_split_candidates)

	best_attribute = min(sampled_split_candidates,
				key=partial(partition_entropy_by, inputs))
	partitions = partition_by(inputs, best_attribute)
	new_candidates = [a for a in split_candidates
				if a != best_attribute]
	subtrees = { attribute_value : build_tree_id3(subset, new_candidates)
	for attribute_value, subset in partitions.items() }
	subtrees[None] = num_trues > num_falses
	return (best_attribute, subtrees)
print(build_tree_random(inputs,2 ))
                             
