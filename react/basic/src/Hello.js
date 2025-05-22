import React from  'react';


function Hello({name, color, isSpecial}) {
    // return(
    //     <div style={{color:props.color}}>Hello~ {props.name}</div>
    // );
    return(
        <div style={{color}}>{isSpecial && <b>*</b>}
            Hello~ {name}</div>
    );

}


Hello.defaultProps = {
    name : 'NoNAme'
}

export default Hello;