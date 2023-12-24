import numpy as np
from ortools.graph.python import min_cost_flow


def main():
    # Paketin çağırılması
    smcf = min_cost_flow.SimpleMinCostFlow()
    # Hatların oluştuğu düğümlerin oluşturulması

    start_nodes = np.array([0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 5])
    # Hatların bittiği düğümlerin yazılması
    end_nodes = np.array([1, 2, 2, 3, 1, 4, 2, 4, 5, 3, 4])
    # Problemi MMAP'ye dönüştürmek için kapasiteleri 1 olarak kabul ederiz
    capacities = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    # Birim maliyetler sorudaki gibidir
    unit_costs = np.array([2, 8, 5, 3, 6, 0, 1, 7, 6, 4, 2])

    # Kaynak düğümünün arzını 1, batak düğümü ise -1 kabul ederiz
    supplies = [1, 0, 0, 0, 0, -1]

    # İşlemlerin yapılması.
    all_arcs = smcf.add_arcs_with_capacity_and_unit_cost(
        start_nodes, end_nodes, capacities, unit_costs
    )

    # Her düğüme arzın eklenmesi
    smcf.set_nodes_supplies(np.arange(0, len(supplies)), supplies)

    # Solve fonksiyonunun çağırılması
    status = smcf.solve()

    if status != smcf.OPTIMAL:
        print("There was an issue with the min cost flow input.")
        print(f"Status: {status}")
        exit(1)
    print(f"Minimum cost: {smcf.optimal_cost()}")
    print("")
    print(" Arc    Flow / Capacity Cost")
    solution_flows = smcf.flows(all_arcs)
    costs = solution_flows * unit_costs
    for arc, flow, cost in zip(all_arcs, solution_flows, costs):
        print(
            f"{smcf.tail(arc):1} -> {smcf.head(arc)}  {flow:3}  / {smcf.capacity(arc):3}       {cost}"
        )


if __name__ == "__main__":
    main()
