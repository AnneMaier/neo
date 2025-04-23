// wordcloud2.js가 먼저 로드되어 있어야 함
// eventNames: ["이벤트명1", "이벤트명2", ...]
window.renderEventNameWordCloud = function(eventNames) {
    // 1. 문장들을 단어 단위(띄어쓰기 기준)로 쪼개서 모두 합침
    let words = [];
    eventNames.forEach(name => {
        words = words.concat(name.split(' '));
    });
    // 2. 단어 빈도 계산
    const freqMap = {};
    words.forEach(word => {
        freqMap[word] = (freqMap[word] || 0) + 1;
    });
    const wordCloudList = Object.entries(freqMap);
    // 3. 마스킹 이미지 준비
    const maskImg = new Image();
    maskImg.src = '/static/korea-mask.png'; // 한반도 실루엣 PNG 경로
    maskImg.onload = function() {
        WordCloud(document.getElementById('wordcloud'), {
            list: wordCloudList,
            gridSize: 10,
            weightFactor: 18,
            fontFamily: 'NanumBarunGothic, sans-serif',
            color: 'random-dark',
            backgroundColor: '#fff',
            rotateRatio: 0, // 회전 없이 정렬
            ellipticity: 0.5, // 타원형으로
            drawOutOfBound: false, // 밖으로 안 나가게
            shape: 'ellipse', // 타원형
            maskImage: maskImg
        });
    };
};
