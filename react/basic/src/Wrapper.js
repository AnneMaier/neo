import React from "react";


function Wrapper({ children}) {
    const style = {
        border : '2px solid black',
        padding : '16pxs'
    }
    return <div style={style}>{children}</div>
}

export default Wrapper;