# Maintainer: Matteo Finazzer <matteo.finazzer AT gmail DOT com>

pkgname=redshift_adjuster
pkgver=0.3
pkgrel=1
pkgdesc="Wrapper CLI for redshift which stores configs and Temperature value"
arch=('any')
#url="" # la repo su git?
license=('GPL')
groups=("MF_env")
depends=("redshift>=1.12" "python>=3.8")
#makedepends=()
#checkdepends=()
#optdepends=()
provides=("redshift")
#conflicts=()
#replaces=()
backup=("etc/$pkgname/config.yaml")
options=()
install=
changelog=
source=("https://github.com/mate377/redshift_adjuster/archive/$pkgver.tar.gz"
	)
noextract=()
md5sums=('SKIP')
validpgpkeys=()

#prepare() {
#	cd "$pkgname-$pkgver"
#	patch -p1 -i "$srcdir/$pkgname-$pkgver.patch"
#}

#build() {
#	cd "$pkgname-$pkgver"
#	./configure --prefix=/usr
#	make
#}

#check() {
#	cd "$pkgname-$pkgver"
#	make -k check
#}

package() {
	echo srcdir: $srcdir
	echo pkgdir: $pkgdir
	echo
	cd "$pkgname-$pkgver"
	#make DESTDIR="$pkgdir/" install

	install -d -m755 "${pkgdir}/usr/bin"
	install -d -m755 "${pkgdir}/usr/share/$pkgname"
	install -d -m755 "${pkgdir}/etc/$pkgname"

	install --mode=755 ./$pkgname.py $pkgdir/usr/bin # bin
	install --mode=755 ./current.yaml $pkgdir/usr/share/$pkgname/ # data
	install --mode=755 ./config.yaml $pkgdir/etc/$pkgname # config
	
}
