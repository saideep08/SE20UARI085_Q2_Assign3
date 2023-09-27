class PatientRecord:
    def __init__(self, patient_name, arrival_time, treatment_duration, urgency_priority):
        self.patient_name = patient_name
        self.arrival_time = arrival_time
        self.treatment_duration = treatment_duration
        self.urgency_priority = urgency_priority

def first_come_first_serve_sort(patients):
    return sorted(patients, key=lambda x: x.arrival_time)

def shortest_job_first_sort(patients):
    return sorted(patients, key=lambda x: x.treatment_duration)

def priority_based_sort(patients):
    return sorted(patients, key=lambda x: -x.urgency_priority)

def round_robin_schedule(patients, time_quantum=10):
    queue = []
    current_time = 0
    execution_sequence = []

    while patients or queue:
        available_patients = [p for p in patients if p.arrival_time <= current_time]
        queue.extend(available_patients)
        for p in available_patients:
            patients.remove(p)

        if queue:
            current_patient = queue.pop(0)
            if current_patient.treatment_duration > time_quantum:
                current_time += time_quantum
                current_patient.treatment_duration -= time_quantum
                queue.append(current_patient)
            else:
                current_time += current_patient.treatment_duration
                execution_sequence.append(current_patient)
        else:
            current_time += 1

    return execution_sequence

patients = [
    PatientRecord('Patient1', 0, 30, 3),
    PatientRecord('Patient2', 10, 20, 5),
    PatientRecord('Patient3', 15, 40, 2),
    PatientRecord('Patient4', 20, 15, 4)
]

fcfs_order = [p.patient_name for p in first_come_first_serve_sort(patients)]
sjf_order = [p.patient_name for p in shortest_job_first_sort(patients)]
ps_order = [p.patient_name for p in priority_based_sort(patients)]
rr_order = [p.patient_name for p in round_robin_schedule(patients)]

print("First Come First Serve Scheduling Order:", fcfs_order)
print("Shortest Job First Scheduling Order:", sjf_order)
print("Priority Based Scheduling Order:", ps_order)
print("Round Robin Scheduling Order:", rr_order)

# Determine the best scheduling algorithm and mention the algorithm name
algorithm_orders = {
    "First Come First Serve Scheduling": fcfs_order,
    "Shortest Job First Scheduling": sjf_order,
    "Priority Based Scheduling": ps_order,
    "Round Robin Scheduling": rr_order
}

best_algorithm_name = min(algorithm_orders, key=lambda x: len(algorithm_orders[x]))
best_algorithm_order = algorithm_orders[best_algorithm_name]

print("The best scheduling algorithm for this case is:", best_algorithm_name)
print("Order of patients for the best algorithm:", best_algorithm_order)
