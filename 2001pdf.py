from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(30, 144, 255) # Blue header color
        self.cell(0, 10, 'Algorithm Design & Analysis Cheat Sheet', 0, 1, 'C')
        self.set_text_color(0) # Reset color
        self.ln(3)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 7, title, 0, 1, 'L', 1)
        self.ln(3)

    def print_table(self, header, data, col_widths, font_size=9):
        # Header
        self.set_font('Arial', 'B', font_size)
        y_start = self.get_y()
        x_start = self.get_x()
        
        # Draw header row
        for i, h in enumerate(header):
            self.cell(col_widths[i], 6, h, 1, 0, 'C')
        self.ln(6) 
        
        # Data rows
        self.set_font('Arial', '', font_size)
        for row in data:
            y = self.get_y()
            if y > 270: # Page break handling
                self.add_page()
                y = self.get_y()
            
            x = self.get_x()
            line_height = 5
            max_lines = 1
            
            # 1. Determine the maximum height needed for this row
            for i, item in enumerate(row):
                # Using string length to estimate height for compatibility
                h_estimate = (len(str(item)) // (col_widths[i] // 3)) + 1
                if h_estimate > max_lines:
                    max_lines = h_estimate
            
            cell_height = max_lines * line_height

            # 2. Draw all columns with the calculated max height
            for i, item in enumerate(row):
                self.rect(x, y, col_widths[i], cell_height) # Draw the cell boundary
                self.set_xy(x, y) # Set position inside cell
                self.multi_cell(col_widths[i], line_height, str(item), 0, 'C') # Draw text
                x += col_widths[i]
            
            self.set_xy(x_start, y + cell_height) # Move to start of next row


pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_margins(10, 10, 10)

# =========================================================================
# SECTION 1: SORTING ALGORITHMS
# =========================================================================
pdf.chapter_title("1. Sorting Algorithms (Comparisons, Swaps & Stability)")

header_sorting = ["Algorithm", "Best Case Time", "Worst Case Time", "Key Metric & Notes"]
data_sorting = [
    ["Insertion Sort", "O(n)", "O(n^2)", 
     "Best: n-1 comps, 0 swaps. Worst: ~ n^2/2 comps/swaps. Stable: Yes."],
    ["Merge Sort", "O(n log n)", "O(n log n)", 
     "Recurrence (Worst): W(n) = 2W(n/2) + n - 1. Space: O(n). Stable: Yes."],
    ["Quick Sort", "O(n log n)", "O(n^2)", 
     "Worst: Pivot is consistently Min/Max. Comparisons: n(n-1)/2. Stable: No."],
    ["Heap Sort", "O(n log n)", "O(n log n)", 
     "Heapify: O(n). deleteMax: O(log n). Total: O(n log n). Stable: No."]
]
pdf.print_table(header_sorting, data_sorting, [30, 35, 35, 90])
pdf.ln(5)

# =========================================================================
# SECTION 2: RECURRENCE RELATIONS
# =========================================================================
pdf.chapter_title("2. Recurrence Relation Analysis (Week 8)")

# --- Master Theorem Table ---
pdf.set_font('Arial', 'B', 10)
pdf.cell(0, 5, "A. Master Theorem: T(n) = aT(n/b) + f(n)", 0, 1)
header_master = ["Case", "Condition", "Result"]
data_master = [
    ["1 (Leaves Win)", "f(n) = O(n^(log_b a - epsilon))", "Theta(n^(log_b a))"],
    ["2 (Tie)", "f(n) = Theta(n^(log_b a) * log^k n)", "Theta(n^(log_b a) * log^(k+1) n)"],
    ["3 (Root Wins)", "f(n) = Omega(n^(log_b a + epsilon))", "Theta(f(n))"]
]
pdf.print_table(header_master, data_master, [35, 100, 55])
pdf.ln(3)

# --- Summation Table ---
pdf.set_font('Arial', 'B', 10)
pdf.cell(0, 5, "B. Summation Formulas (Iteration Method)", 0, 1)
header_sum = ["Type", "Pattern / Work", "Formula / Result", "Big-Theta"]
data_sum = [
    ["AP (Arithmetic)", "1 + 2 + ... + n", "n(n+1)/2", "Theta(n^2)"],
    ["GP (Decaying)", "Ratio r < 1", "Sum approx. First Term", "Theta(largest term)"],
    ["GP (Growing)", "Ratio r > 1", "Sum approx. Last Term (Leaves)", "Theta(leaves cost)"]
]
pdf.print_table(header_sum, data_sum, [30, 60, 60, 40])
pdf.ln(5)

# =========================================================================
# SECTION 3: GRAPH & TREE ALGORITHMS
# =========================================================================
pdf.chapter_title("3. Graph & Tree Algorithms (Weeks 4-7)")
header_graph = ["Algorithm", "Time Complexity", "Key Restriction / Purpose"]
data_graph = [
    ["BFS / DFS", "O(V + E)", "Traversal (visiting all nodes)."],
    ["Topological Sort", "O(V + E)", "Must be a DAG. Uses DFS (reverse finish time)."],
    ["Dijkstra's", "O(E log V)", "No negative weights. Finds SSSP."],
    ["Prim's (MST)", "O(E log V)", "Grows a tree from one starting node. Works with negative weights."],
    ["Kruskal's (MST)", "O(E log E)", "Processes edges globally. Uses Union-Find for cycle detection."],
    ["Union-Find Ops (WQU+PC)", "O(M log* N) ~ O(M)", "Cycle detection for Kruskal's."]
]
pdf.print_table(header_graph, data_graph, [40, 35, 115])
pdf.ln(5)

# =========================================================================
# SECTION 4: DP & GREEDY
# =========================================================================
pdf.chapter_title("4. Dynamic Programming & Greedy (Weeks 9-11)")
header_dp = ["Problem", "Approach", "Time Complexity", "Notes"]
data_dp = [
    ["Fractional Knapsack", "Greedy", "O(n log n)", "Sort by Value/Weight ratio. Always optimal."],
    ["Interval Scheduling", "Greedy", "O(n log n)", "Sort by Earliest Finish Time. Always optimal."],
    ["0/1 Knapsack", "DP", "O(n * W)", "Pseudo-polynomial. W = capacity."],
    ["LCS", "DP", "O(n * m)", "n, m are string lengths. Recurrence involves max(subproblems)."]
]
pdf.print_table(header_dp, data_dp, [45, 30, 40, 75])
pdf.ln(5)

# =========================================================================
# SECTION 5: STRING MATCHING
# =========================================================================
pdf.chapter_title("5. String Matching Algorithms (Week 12)")
header_sm = ["Algorithm", "Best Case Comps", "Worst Case Comps", "Notes"]
data_sm = [
    ["Brute Force", "O(n)", "O(mn)", "Worst case: m(n-m+1) comps."],
    ["Rabin-Karp", "O(n+m)", "O(mn)", "Uses hashing (mod q) and radix (d). Worst case: spurious hits."],
    ["Boyer-Moore", "O(n/m)", "O(mn)", "Sublinear in best/average case. Uses charJump and matchJump."]
]
pdf.print_table(header_sm, data_sm, [40, 40, 40, 70])
pdf.ln(5)

# =========================================================================
# SECTION 6: COMPLEXITY CLASSES
# =========================================================================
pdf.chapter_title("6. Complexity Classes & Hard Problems (Week 13)")
header_cc = ["Class / Problem", "Time Complexity", "Classification"]
data_cc = [
    ["P (Deterministic Poly)", "O(n^k)", "P"],
    ["NP (Nondeterministic Poly)", "Unknown", "NP"],
    ["TSP (Decision)", "Unknown (Worst: O(n!))", "NP-Complete"],
    ["Towers of Hanoi", "O(2^n)", "Exponential Time"]
]
pdf.print_table(header_cc, data_cc, [55, 65, 60])
pdf.ln(5)

pdf.set_font('Arial', 'I', 10)
pdf.multi_cell(0, 5, "Disclaimer: These tables summarize theoretical worst-case complexities. Actual runtime depends on constants and input structure.")


pdf.output("Algorithm_Cheatsheet.pdf")