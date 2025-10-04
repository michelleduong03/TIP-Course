# Problem 1
def manage_stage_changes(changes):
    scheduled = []
    canceled = []

    for action in changes:
        if action.startswith("Schedule"):
            _, perf_id = action.split() # throwaway variable, performance ID
            scheduled.append(perf_id)
        elif action == "Cancel":
            if scheduled: 
                canceled.append(scheduled.pop())
        elif action == "Reschedule":
            if canceled:
                scheduled.append(canceled.pop())
    
    return scheduled


print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 

# Problem 2
def process_performance_requests(requests):
    queue = requests[:] # make a copy of requests
    result = [] # final order of processed performances

    while queue: # while there are still requests left
        # find the request with the highest priority
        max_priority = -1
        max_index = -1
        for i in range(len(queue)):
            if queue[i][0] > max_priority: # compare priorities
                max_priority = queue[i][0]
                max_index = i

        # remove that request from queue and add its name to result
        _, performance = queue.pop(max_index)
        result.append(performance)

    return result

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))

# Problem 3

# Problem 4

# Problem 5

# Problem 6

# Problem 7

