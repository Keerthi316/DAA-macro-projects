public class NQueens {

    static int N = 4;
    static int[] board = new int[N];

    static boolean safe(int row, int col) {
        for (int r = 0; r < row; r++) {

            // Same column
            if (board[r] == col)
                return false;

            // Same diagonal
            if (Math.abs(r - row) == Math.abs(board[r] - col))
                return false;
        }

        return true;
    }

    static void solve(int row) {
        if (row == N) {
            printBoard();
            return;
        }

        for (int col = 0; col < N; col++) {

            if (safe(row, col)) {
                board[row] = col;

                solve(row + 1);

                board[row] = -1;   // Backtrack
            }
        }
    }

    static void printBoard() {
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (board[r] == c)
                    System.out.print("Q ");
                else
                    System.out.print(". ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void main(String[] args) {
        solve(0);
    }
}