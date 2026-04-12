from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    error = None

    if request.method == "POST":
        try:
            harga = request.form.get("harga")
            jumlah = request.form.get("jumlah")
            diskon = request.form.get("diskon")

            harga = float(harga) if harga else None
            jumlah = float(jumlah) if jumlah else None
            diskon = float(diskon) if diskon else 0

            if harga is not None and jumlah is not None:
                total = harga * jumlah
                potongan = total * (diskon / 100)
                hasil = total - potongan

                rumus = "Pendapatan = (Harga × Jumlah) - Diskon%"
            else:
                error = "Isi harga dan jumlah!"

        except ValueError:
            error = "Input harus berupa angka!"

        return render_template("aboutfina.html", hasil=hasil, error=error, rumus=rumus if not error else None)

    return render_template("aboutfina.html", hasil=None, error=None, rumus=None)


if __name__ == "__main__":
    app.run(debug=True)
