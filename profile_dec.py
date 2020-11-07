import cProfile
import io, pstats


# Profiler decorator
def profile(func):

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        # Enable profiling
        pr.enable()
        # Execute the function
        ret_val = func(*args, **kwargs)
        # Disable profiling
        pr.disable()
        ios = io.StringIO()
        ps = pstats.Stats(pr, stream=ios).sort_stats('calls')
        ps.print_stats()
        # Save stats
        # ps.dump_stats('output.pstats')
        print(ios.getvalue())
        # Return the function value
        return ret_val

    return inner