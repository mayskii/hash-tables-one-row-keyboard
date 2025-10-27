# def typing_time(layout, word):
#     curr_pos = 0
#     total_time = 0

#     for letter in word:
#         letter_pos = 0
#         for key in layout:
#             if key == letter:
#                 break
#             letter_pos += 1 # letter position found
        
#         time = abs(letter_pos - curr_pos)
#         total_time += time
#         curr_pos = letter_pos
    
#     return total_time





# layout = "abcd"
# (0, 'a'), (1, 'b'), (2, 'c'), (3, 'd') - how enumerate works 

def typing_time(layout, word):
    positions = {letter: pos for pos, letter in enumerate(layout)}
    location = 0
    tiped_time = 0

    for letter in word:
        next_loc = positions[letter]
        time = abs(next_loc - location)
        tiped_time += time
        location = next_loc

    return tiped_time



