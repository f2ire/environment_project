def comaIntoDot(iteration: int, max_iteration: int) -> str:
    if iteration != max_iteration - 1:
        return ", "
    else:
        return "."
