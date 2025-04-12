# HOW TO USE
`instructions.txt`:
- Each instruction goes on one line.
- Format: `<expected_state> <expected_data> <new_state> <new_data> <L/R>`

`input.txt`:
- One line contain a string of `0`, `1`, `*` and `B`
- `0` and `1` are the two states of the cell.
- `*` is the empty cell (use for splitting number).
- `B` is the boundary cell.

> ![NOTE] About number detection
> 
> Each full of `1` strings is considered as a number.
> Value is `<number of 1> - 1`, for example `1111` is `3`.
