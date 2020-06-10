from flask import Flask

app = Flask(__name__)

data = {
    "telp": [
        {
            "id": "telp1",
            "image_url": "https://storage.googleapis.com/vutura/assets/images/c821b839-1d1a-4098-80cb-981e2f9be6cb.jpg",
            "title": "Paket Telpon 3 Hari",
            "desc": "Bisa nelpon kemana aja sepuasnya selama 3 hari. Cuma Rp 2000 aja!",
            "active": "7 Hari",
            "price": "Rp 2000"
        },
        {
            "id": "telp2",
            "image_url": "https://storage.googleapis.com/vutura/assets/images/c821b839-1d1a-4098-80cb-981e2f9be6cb.jpg",
            "title": "Paket Telpon Seminggu",
            "desc": "Bisa nelpon kemana aja sepuasnya selama seminggu. Cuma Rp 5000 aja!",
            "active": "7 Hari",
            "price": "Rp 5000"
        },
        {
            "id": "telp3",
            "image_url": "https://storage.googleapis.com/vutura/assets/images/c821b839-1d1a-4098-80cb-981e2f9be6cb.jpg",
            "title": "Paket Telpon Sebulan",
            "desc": "Bisa nelpon kemana aja sepuasnya selama sebulan. Cuma Rp 20000 aja!",
            "active": "30 Hari",
            "price": "Rp 20000"
        }
    ],
    "sms": [
        {
            "id": "sms1",
            "image_url": "https://image.freepik.com/free-icon/messages_318-10574.jpg",
            "title": "Paket SMS 3 Hari",
            "desc": "Bisa SMS kemana aja sepuasnya selama 3 hari. Cuma Rp 2000 aja!",
            "active": "3 Hari",
            "price": "Rp 2000"
        },
        {
            "id": "sms2",
            "image_url": "https://image.freepik.com/free-icon/messages_318-10574.jpg",
            "title": "Paket SMS Seminggu",
            "desc": "Bisa SMS kemana aja sepuasnya selama seminggu. Cuma Rp 5000 aja!",
            "active": "7 Hari",
            "price": "Rp 5000"
        },
        {
            "id": "sms3",
            "image_url": "https://image.freepik.com/free-icon/messages_318-10574.jpg",
            "title": "Paket SMS Sebulan",
            "desc": "Bisa SMS kemana aja sepuasnya selama sebulan. Cuma Rp 15000 aja!",
            "active": "30 Hari",
            "price": "Rp 15000"
        }
    ],
    "kuota":[
        {
            "id": "kuota1",
            "image_url": "https://tastythailand.com/wp-content/uploads/2014/03/internet.jpg",
            "title": "Paket Internet 500MB",
            "desc": "Bisa internetan sepuasnya dengan kuota 500MB, masa aktif selama 7 hari.",
            "active": "7 Hari",
            "price": "Rp 15000"
        },
        {
            "id": "kuota2",
            "image_url": "https://tastythailand.com/wp-content/uploads/2014/03/internet.jpg",
            "title": "Paket Internet 5GB",
            "desc": "Bisa internetan sepuasnya dengan kuota 5GB, masa aktif selama 30 hari.",
            "active": "30 Hari",
            "price": "Rp 60000"
        },
        {
            "id": "kuota3",
            "image_url": "https://tastythailand.com/wp-content/uploads/2014/03/internet.jpg",
            "title": "Paket Internet 50GB",
            "desc": "Bisa internetan sepuasnya dengan kuota 50GB, masa aktif selama 60 hari.",
            "active": "60 Hari",
            "price": "Rp 120000"
        }
    ],
    "promo": [
        {
            "id": "promo1",
            "image_url": "https://www.expertaidrepair.com/wp-content/uploads/2019/04/240_F_115982009_Kgy5bUrHo1zM6PYlC4rLtCJCULFlOf8Y.jpg",
            "title": "Paket Bundle 1",
            "desc": "Bisa Telpon dan SMS sepuasnya plus Internetan dengan kuota 500MB. Berlaku selama 7 Hari.",
            "active": "7 Hari",
            "price": "Rp 20000"
        },
        {
            "id": "promo2",
            "image_url": "https://www.expertaidrepair.com/wp-content/uploads/2019/04/240_F_115982009_Kgy5bUrHo1zM6PYlC4rLtCJCULFlOf8Y.jpg",
            "title": "Paket Bundle 2",
            "desc": "Bisa Telpon dan SMS sepuasnya plus Internetan dengan kuota 5GB. Berlaku selama 30 Hari.",
            "active": "30 Hari",
            "price": "Rp 90000"
        },
        {    
            "id": "promo3",
            "image_url": "https://www.expertaidrepair.com/wp-content/uploads/2019/04/240_F_115982009_Kgy5bUrHo1zM6PYlC4rLtCJCULFlOf8Y.jpg",
            "title": "Paket Bundle 3",
            "desc": "Bisa Telpon dan SMS sepuasnya plus Internetan dengan kuota 50GB. Berlaku selama 60 Hari.",
            "active": "60 Hari",
            "price": "Rp 200000"
        }
    ] 
}

@app.route('/paket/<kategori>')
def cek_paket(kategori):
    json = {
        "chats": []
    }
    for i in data[kategori]:
        json["chats"].append(
            {
                "columns": [
                    {
                    "image_url": i["image_url"],
                    "title": i["title"],
                    "text": i["desc"],
                    "buttons": [
                        {
                        "label": "Pesan",
                        "type": "path",
                        "path": "5ed9fdac20f8374bf65abcaa",
                        "variable": {
                            "kategori": kategori,
                            "id": i["id"]
                            }
                        }
                    ],
                    "type": "button"
                    }
                ],
                "type": "carousel"
            },
        )
    return json

@app.route('/konfirmasi/<kategori>/<id>')
def konfirmasi(kategori,id):
    idx = 0
    while data[kategori][idx]["id"] != id:
        idx +=1
    return {
        "chats": [
            {
                "text": str(data[kategori][idx]["title"]) + 
                        "\nMasa Aktif : " + str(data[kategori][idx]["active"]) +
                        "\nHarga : " + str(data[kategori][idx]["price"]) +
                        "\nApakah Anda yakin ingin memesan?",
                "buttons": [
                    {
                        "label": "Pesan",
                        "type": "path",
                        "path": "5edc7faf20f8374bf65ac4e3",
                        "variable": {
                            "kategori": kategori,
                            "id" : id
                        }
                    },
                    {
                        "label": "Tidak",
                        "type": "path",
                        "path": "5ed9d66e20f8374bf65abb63",
                    }
                ],
                "type": "button"  
            }
        ]
    }

@app.route('/pesan/<kategori>/<id>')
def pesan(kategori,id):
    idx = 0
    while data[kategori][idx]["id"] != id:
        idx +=1
    return {
        "chats": [
            {
                "text": "Selamat! Anda berhasil membeli " + str(data[kategori][idx]["title"]) + " yang aktif selama " + str(data[kategori][idx]["active"]),
                "type": "text"
            } 
        ]
    }
    
if __name__ == "__main__":
    app.run()