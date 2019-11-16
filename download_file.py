import requests
import sys


def download_filename(url, save_path):
    """
        Function that downloads a file from an url.

        Example:
            # downloads a cat image :)
            download_filename("https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg", "cat.jpg")


        Attributes:
            url (str): Corresponding url of the image.
            save_path (str): Saving path of the file.
    """
    print("\nDownloading `{}`.".format(url))

    with open(save_path, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')

        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total / 1000), 1024 * 1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50 * downloaded / total)
                sys.stdout.write('\r[{}{}{}] {}/{} {}%'.format('=' * (done-1), ">",  '.' * (50 - done),
                                                               int((done*2) * total/100), total, done*2))
                sys.stdout.flush()
    sys.stdout.write('\n\n')