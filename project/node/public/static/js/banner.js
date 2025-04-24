fetch('http://192.168.1.28:5000/posters')
  .then(res => res.json())
  .then(posters => {
    // 중복 url 방지: posters 배열에서 중복 url 제거
    const uniquePosters = posters.filter(
      (poster, idx, self) =>
        idx === self.findIndex(p => p.url === poster.url)
    );

    function setBanner(selector, poster) {
      const banner = document.querySelector(selector);
      banner.innerHTML = `
        <img src="${poster.url}" alt="포스터">
        <div class="banner-caption">${poster.title || ''}</div>
      `;
    }
    if (uniquePosters.length > 1) {
        let leftIdx = Math.floor(Math.random() * uniquePosters.length);
        let rightIdx;
        do {
          rightIdx = Math.floor(Math.random() * uniquePosters.length);
        } while (rightIdx === leftIdx);
      
        setBanner('.ad-left', uniquePosters[leftIdx]);
        setBanner('.ad-right', uniquePosters[rightIdx]);
      }
    function updateBannerPosition() {
      const scrollY = window.scrollY || window.pageYOffset;
      document.querySelectorAll('.ad-banner').forEach(banner => {
        banner.style.top = (300 + scrollY) + 'px';
      });
    }
    window.addEventListener('scroll', updateBannerPosition);
    window.addEventListener('resize', updateBannerPosition);
    document.addEventListener('DOMContentLoaded', updateBannerPosition);
  });