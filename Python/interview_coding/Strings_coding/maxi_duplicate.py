# Input (list of votes)
votes = ['john', 'johnny', 'jackie', 'johnny', 'john', 'jackie', 'jamie', 'jamie', 'john', 'johnny', 'jamie', 'johnny', 'john']

# Dictionary to store vote counts
vote_count = {}

# Counting votes for each candidate
for vote in votes:
    if vote not in vote_count:
        vote_count[vote] = 1  # Initialize count for the candidate
    else:
        vote_count[vote] += 1  # Increment count for the candidate

# Manually find the candidate with the maximum votes
max_votes = -1
winner = ""

# Iterate through the dictionary
for candidate in vote_count:
    if vote_count[candidate] > max_votes:
        max_votes = vote_count[candidate]
        winner = candidate
    elif vote_count[candidate] == max_votes:
        # Tie-breaking by lexicographical order
        if candidate < winner:
            winner = candidate

# Output the winner and their vote count
print(winner, max_votes)
