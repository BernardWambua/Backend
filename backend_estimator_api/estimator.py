import math


def estimator(data):
    time_to_elapse = data["timeToElapse"]
    period_type = data["periodType"]
    if period_type == 'weeks':
        time_to_elapse = time_to_elapse * 7
    elif period_type == 'months':
        time_to_elapse = time_to_elapse * 30
    else:
        pass

    currently_infected = data["reportedCases"] * 10
    severe_currently_infected = data["reportedCases"] * 50
    power_factor = time_to_elapse // 3
    infections_by_requested_time = currently_infected * 2**power_factor
    severe_infections_by_requested_time = severe_currently_infected * 2 ** power_factor

    severe_cases_by_requested_time = math.trunc(
        0.15 * infections_by_requested_time)
    severe_severe_cases_by_requested_time = math.trunc(
        0.15 * severe_infections_by_requested_time)
    hospital_beds_by_requested_time = math.trunc((0.35 *
                                                  data["totalHospitalBeds"] - severe_cases_by_requested_time))
    severe_hospital_beds_by_requested_time = math.trunc((
        0.35 * data["totalHospitalBeds"] - severe_severe_cases_by_requested_time))

    cases_for_icu_by_requested_time = math.trunc(
        0.05 * infections_by_requested_time)
    severe_cases_for_icu_by_requested_time = math.trunc(
        0.05 * severe_infections_by_requested_time)
    cases_for_ventilators_by_requested_time = math.trunc(
        0.02 * infections_by_requested_time)
    severe_cases_for_ventilators_by_requested_time = math.trunc(
        0.02 * severe_infections_by_requested_time)

    dollars_in_flight = math.trunc((infections_by_requested_time * data["region"]["avgDailyIncomePopulation"]) *
                                   data["region"]["avgDailyIncomeInUSD"] * time_to_elapse)
    severe_dollars_in_flight = math.trunc((severe_infections_by_requested_time *
                                           data["region"]["avgDailyIncomePopulation"]) * data["region"]["avgDailyIncomeInUSD"] * time_to_elapse)

    return {
        "data": data,
        "impact": {"currentlyInfected": currently_infected,
                   "infectionsByRequestedTime": infections_by_requested_time,
                   "severeCasesByRequestedTime": severe_cases_by_requested_time,
                   "hospitalBedsByRequestedTime": hospital_beds_by_requested_time,
                   "casesForICUByRequestedTime": cases_for_icu_by_requested_time,
                   "casesForVentilatorsByRequestedTime": cases_for_ventilators_by_requested_time,
                   "dollarsInFlight": dollars_in_flight
                   },
        "severeImpact": {"currentlyInfected": severe_currently_infected,
                         "infectionsByRequestedTime": severe_infections_by_requested_time,
                         "severeCasesByRequestedTime": severe_severe_cases_by_requested_time,
                         "hospitalBedsByRequestedTime": severe_hospital_beds_by_requested_time,
                         "casesForICUByRequestedTime": severe_cases_for_icu_by_requested_time,
                         "casesForVentilatorsByRequestedTime": severe_cases_for_ventilators_by_requested_time,
                         "dollarsInFlight": severe_dollars_in_flight
                         }

    }
