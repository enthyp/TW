def trace(execution, system):
    init = list(execution)
    trace_set = {execution}
    ind_relation = system.ind_relation    

    def trace_recursive(execution, trace_set):
        for i in range(len(execution) - 1):
            if execution[i] in ind_relation[execution[i + 1]]:
                execution[i], execution[i + 1] = execution[i + 1], execution[i]
                new_execution = ''.join(execution)
                if not new_execution in trace_set:
                    trace_set.add(new_execution)
                    trace_recursive(execution, trace_set)               
                execution[i], execution[i + 1] = execution[i + 1], execution[i]

    trace_recursive(init, trace_set)    
    return trace_set 

