# Maintainer: Matteo Finazzer <matteo.finazzer AT gmail DOT com>

pkgname=redshift-adjuster
pkgver=0.1
pkgrel=1
pkgdesc="Wrapper CLI for redshift which stores configs and Temperature value"
arch=('any')
#url="" # la repo su git?
license=('GPL')
groups=("MF_env")
depends=("redshift>=1.12")
#makedepends=()
#checkdepends=()
#optdepends=()
provides=("redshift")
#conflicts=()
#replaces=()
backup=()
options=()
install=
changelog=
source=("$pkgname-$pkgver.tar.gz"
        "$pkgname-$pkgver.patch")
noextract=()
md5sums=()
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
	#cd "$pkgname-$pkgver"
	#make DESTDIR="$pkgdir/" install
	$pkgdir/usr/bin/$pkgname.py # bin
	$pkgdir/usr/share/$pkgname/current.yaml # data
	$pkgdir/etc/$pkgname/config.yaml # config
	
}
