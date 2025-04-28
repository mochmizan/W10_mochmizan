#Soal 3
class Buku:
  def cover(self):
    pass
class Novel(Buku):
  def cover(self):
    return "Novel memiliki Soft Cover"
class Ensiklopedia(Buku):
  def cover(self):
    return "Ensiklopedia memiliki Hard Cover"
class Factory:
  @staticmethod
  def buat_buku(jenis_buku):
    if jenis_buku == "Novel":
      return Novel()
    elif jenis_buku == "Ensiklopedia":
      return Ensiklopedia()
    else:
      raise ValueError("Jenis buku ini belum ada")

Twilight = Factory.buat_buku("Novel")
print(Twilight.cover())
