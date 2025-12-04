from pathlib import Path
from rich.console import Console
from rich.live import Live
from rich.text import Text
from rich.panel import Panel
from rich.layout import Layout
import time

PUZZLE_INPUT_PATH = Path("day-4/puzzle-input.txt")


def get_puzzle_input(path: Path) -> str:
    with open(path, "r") as f:
        raw_input = f.read()
    return raw_input


def check_adjacent_coords(matrix: list, i: int, j: int, n: int, symbol='@'):
    """Checks adjacent coords which are n distances away from (i, j) for presence of symbol"""
    paper_count = 0

    for a in range(i - n, i + n + 1):
        for b in range(j - n, j + n + 1):
            if a == i and b == j:
                pass
            elif a < 0 or b < 0 or a >= len(matrix) or b >= len(matrix[0]):
                pass
            else:
                if matrix[a][b] == '@':
                    paper_count += 1

    return paper_count


def render_matrix(matrix, removable=None, stats=None):
    """Render the matrix with highlighting for removable items"""
    removable_set = set(removable) if removable else set()
    
    # Create the matrix visualization
    output = Text()
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if (i, j) in removable_set:
                # Highlight removable items in bright red
                output.append(f"{val} ", style="bold bright_red on black")
            elif val == '@':
                # Regular paper in yellow
                output.append(f"{val} ", style="yellow")
            else:
                # Empty spaces in dim
                output.append(f"{val} ", style="dim white")
        output.append("\n")
    
    # Create stats panel
    stats_text = Text()
    if stats:
        stats_text.append(f"Pass: {stats['pass']}\n", style="bold cyan")
        stats_text.append(f"Reachable this pass: {stats['reachable']}\n", style="green")
        stats_text.append(f"Total removed: {stats['total_removed']}\n", style="bright_magenta")
        stats_text.append(f"Remaining: {stats['remaining']}\n", style="yellow")
    
    # Combine into layout
    layout = Layout()
    layout.split_column(
        Layout(Panel(output, title="Matrix State", border_style="blue"), size=len(matrix) + 2),
        Layout(Panel(stats_text, title="Statistics", border_style="green"), size=7)
    )
    
    return layout


def visualize_removal(matrix, delay=0.3):
    """Main visualization loop"""
    console = Console()
    total_removed = 0
    pass_num = 0
    
    with Live(console=console, refresh_per_second=10) as live:
        while True:
            pass_num += 1
            reachable_count = 0
            removable = []
            
            # Find removable items
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == '@':
                        paper_count = check_adjacent_coords(matrix, i, j, 1)
                        if paper_count < 4:
                            reachable_count += 1
                            removable.append((i, j))
            
            # Count remaining papers
            remaining = sum(row.count('@') for row in matrix)
            
            # Show what will be removed
            stats = {
                'pass': pass_num,
                'reachable': reachable_count,
                'total_removed': total_removed,
                'remaining': remaining
            }
            live.update(render_matrix(matrix, removable, stats))
            time.sleep(delay)
            
            # Remove items
            if removable:
                for i, j in removable:
                    matrix[i][j] = '.'
                total_removed += reachable_count
                
                # Show after removal
                stats['total_removed'] = total_removed
                stats['remaining'] = remaining - reachable_count
                live.update(render_matrix(matrix, None, stats))
                time.sleep(delay)
            else:
                break
        
        # Final state
        time.sleep(1)
    
    console.print(f"\n[bold green]✓ Complete! Total removed: {total_removed}[/bold green]")
    return total_removed


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(PUZZLE_INPUT_PATH)
    matrix = [list(x) for x in puzzle_input.split('\n')]
    
    # Adjust delay here (seconds between frames)
    total_removed = visualize_removal(matrix, delay=0.5)