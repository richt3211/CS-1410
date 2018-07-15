"""
DNA Sequencing
Richard Timpson
CS 1410 T-R 9:00 AM - 10:15 AM

Write your code in this file.

DO NOT RENAME THIS FILE
if you do, the unittests will not run.
"""
import os.path
def fileToList(filename):
	empty_list = []
	print (os.path.exists(filename))
	if os.path.exists(filename):
		file = open(filename, "r")
		lines = file.readlines()
		lines = [x.strip() for x in lines]
		file.close()
		return lines
	else:
		return empty_list
def returnFirstString(strings):
	empty_string = ""
	if not strings:
		return empty_string
	else:
		return strings[0]
def strandsAreNotEmpty(strand1,strand2):
	if strand1 and strand2:
		return True	
def strandsAreEqualLengths(strand1, strand2):
	if len(strand1) == len(strand2):
		return True
def findLargestOverlap(target, candidate):
	if not target and not candidate:
		return -1
	if len(target) != len(candidate):
		return -1
	length = len(target)
	overlap = 0
	for x in range(length):
		print ('target')
		print (target[length -x -1: length])
		print ('candidate')
		print (candidate[0: x +1])
		if target[length - x - 1: length] == candidate[0: x + 1]:
			overlap = x + 1
	if not overlap:
		return (0)
	else:
		return overlap
def findBestCandidate(target, string):
	overlap = []
	for x in range(len(string)):
		overlap.append(findLargestOverlap(target, string[x]))
	best_Candidate_Length = max(overlap)
	best_Candidate = overlap.index(best_Candidate_Length)
	if overlap[best_Candidate] == 0:
		return ('', 0)
	return (string[best_Candidate], overlap[best_Candidate])
def joinTwoStrands(target, candidate, overlap):
	string = ''
	length = len(target)
	new_target = target[0: length - overlap]
	new_candidate = candidate[0: length]
	string = new_target + new_candidate
	return string
def main ():
	target_file = input('Target strand filename: ')
	candidate_file = input('Candidate strands filename: ')
	target_file_list = fileToList(target_file)
	candidate_file_list = fileToList(candidate_file)
	target = returnFirstString(target_file_list)
	overlap = findBestCandidate(target, candidate_file_list)
	string = joinTwoStrands(target,overlap(0), overlap(1))
	print (string)
if __name__ == '__main__':
	main()
