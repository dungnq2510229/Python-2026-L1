import gzip
import pickle
import threading
import os

class BackgroundSaver:
    def __init__(self):
        self._current_thread = None

    def save_async(self, data, filename="student_data.pkl.gz"):
        """
        Starts a background thread to compress and pickle data,
        preventing blocking of the main thread.
        """
        self._current_thread = threading.Thread(
            target=self._save_task, 
            args=(data, filename),
            daemon=True
        )
        self._current_thread.start()

    def _save_task(self, data, filename):
        try:
            with gzip.open(filename, "wb") as f:
                pickle.dump(data, f)
            print(f"\n[Background Thread] Data successfully saved and compressed to {filename}")
        except Exception as e:
            print(f"\n[Background Thread Error] Failed to save data: {e}")

    def wait_till_finished(self):
        """Ensures background save finishes before program exit."""
        if self._current_thread and self._current_thread.is_alive():
            self._current_thread.join()

saver = BackgroundSaver()

def save_data(data, filename="student_data.pkl.gz"):
    """Trigger background save"""
    saver.save_async(data, filename)

def load_data(filename="student_data.pkl.gz"):
    """Load data synchronously (needed at startup)"""
    if not os.path.exists(filename):
        return None
    try:
        with gzip.open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as e:
        print(f"Error loading data: {e}")
        return None