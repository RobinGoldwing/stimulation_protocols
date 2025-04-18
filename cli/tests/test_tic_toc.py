# cli/tests/test_tic_toc.py

# =============================================================================
# XTIM – Experimental Toolkit for Multimodal Neuroscience
# =============================================================================
# Part of the XSCAPE Project (Experimental Science for Cognitive and Perceptual Exploration)
#
# Developed by:
#   - Arturo-José Valiño
#   - Rubén Álvarez-Mosquera
#
# This software is designed to facilitate the creation, execution, and analysis
# of neuroscience experiments involving eye-tracking, EEG, and other modalities.
# It integrates with hardware and software tools such as Pupil Labs, Emobit,
# and MilliKey MH5, providing a unified command-line interface and interactive
# menu system for experiment management.
#
# For more information about the XSCAPE project, please refer to the project's
# documentation or contact the developers.
# =============================================================================


from rich import print
import time

def run():
    print("\n[bold cyan]XTIM — Tic-Toc Timing Precision Test[/bold cyan]")
    print("[dim]This test measures the elapsed time between 'tic' and 'toc' calls.[/dim]\n")

    durations = []
    rounds = 3
    delay_sec = 5

    for i in range(rounds):
        print(f"⏱️  Round {i+1} — sleeping for {delay_sec} seconds...")
        start = time.perf_counter()
        time.sleep(delay_sec)
        end = time.perf_counter()
        elapsed = end - start
        durations.append(elapsed)
        print(f"✅  Elapsed time: {elapsed:.6f} seconds\n")

    mean_time = sum(durations) / len(durations)
    deviation = (sum((x - mean_time) ** 2 for x in durations) / len(durations)) ** 0.5

    print("[bold green]📊 Timing Summary:[/bold green]")
    print(f"  🔁 Rounds        : {rounds}")
    print(f"  ⏱️  Target delay  : {delay_sec:.2f} s")
    print(f"  📈 Mean elapsed  : {mean_time:.6f} s")
    print(f"  📉 Std deviation : {deviation:.6f} s")

    if deviation > 0.01:
        print("[yellow]⚠️  System timing may be unstable. Consider closing background apps.[/yellow]")
    else:
        print("[green]🟢 Timing appears stable.[/green]")
