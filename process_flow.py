import openpyxl


def process_flow(file_path):
    try:
        workbook = openpyxl.load_workbook(file_path)
        worksheet = workbook["Dev-Lofi - V01"]
        rows = worksheet.iter_rows(min_row = 2, max_col = 9)
        for a, b, c, d, e, f, g, h, i in rows:
            if a.value is None:
                break
            else:
                print("Será aqui que todo fluxo do processo irá ocorrer: ")
                track_number = a.value
                track_author_title = b.value
                track_title = c.value
                track_author = d.value
                track_url = e.value
                track_bpm = f.value
                track_mp3_audio = g.value
                track_wav_audio = h.value
                track_duration = i.value
                print(f"Current Track Number: {track_number}")
                print(f"Current Author & Title: {track_author_title}")
                print(f"Current Track Title: {track_title}")
                print(f"Current Track Author: {track_author}")
                print(f"Current Track URL: {track_url}")
                print(f"Current Track BPM: {track_bpm}")
                print(f"Current Track MP3 Audio Status: {track_mp3_audio}")
                print(f"Current Track Wav Audio Status:: {track_wav_audio}")
                print(f"Current Track Duration: {track_duration}")
                print("***********************************************************************************************")
    except Exception as e:
        print(f"An Exception has occurred:\n[{e}]")
