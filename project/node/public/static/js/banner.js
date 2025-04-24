fetch('http://192.168.1.28:5000/posters')
  .then(res => res.json())
  .then(posters => {
    if (posters.length > 1) {
      // 서로 다른 두 개의 인덱스 뽑기
      let leftIdx = Math.floor(Math.random() * posters.length);
      let rightIdx;
      do {
        rightIdx = Math.floor(Math.random() * posters.length);
      } while (rightIdx === leftIdx);

      document.querySelector('.ad-left img').src = posters[leftIdx].url;
      document.querySelector('.ad-right img').src = posters[rightIdx].url;
    } else if (posters.length === 1) {
      // 포스터가 1개뿐이면 양쪽에 동일하게 출력
      document.querySelector('.ad-left img').src = posters[0].url;
      document.querySelector('.ad-right img').src = posters[0].url;
    }
  });

  function updateBannerPosition() {
    const scrollY = window.scrollY || window.pageYOffset;
    // 최소 100px, 최대(원하는 값)까지 제한 가능
    document.querySelectorAll('.ad-banner').forEach(banner => {
      banner.style.top = (300 + scrollY) + 'px';
    });
  }
  window.addEventListener('scroll', updateBannerPosition);
  window.addEventListener('resize', updateBannerPosition);
  document.addEventListener('DOMContentLoaded', updateBannerPosition);