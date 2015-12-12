import Data.Map

type Pos = (Int, Int)
type Grid = Map Pos Bool

data Instruction = On Pos Pos | Off Pos Pos | Toggle Pos Pos 



change_grid_1 :: Grid -> Instruction -> Grid
change_grid_1 grid



fromList [((i, j), False) | i <- [0..999], j <- [0..999]]
