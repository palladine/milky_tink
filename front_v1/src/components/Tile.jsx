export default function Tile({share_datas, cell_datas, onRemove}) {

    return (
        
        <div style={{
            display: 'flex',
            fontSize: '14px',
            justifyContent: 'space-around',
            alignItems: 'center'
        }}>
                <section
                    style={{
                        backgroundColor: share_datas.vol >= cell_datas.limit ? share_datas.state === 'bid' ? '#ffcbcbd8' : '#a9ffa9e0' : '#eeeeee77',
                        transition: 'all 0.6s',
                        display: 'flex',
                        flexDirection: 'row',
                        alignItems: 'center',
                        width: '170px',
                        height: '23px',
                        flexBasis: '170px',
                        justifyContent: 'space-around'
                    }}
                >
                    <div>{cell_datas.share.ticker}</div>
                    <div><b>{share_datas.price}</b></div> 
                    <div>{share_datas.vol}</div>
                    
                    <div>
                        <a href="#" onClick={(e) => {
                            e.preventDefault();
                            e.stopPropagation();
                            onRemove(cell_datas.num_cell);
                        }}
                        style={{
                            textDecoration: 'none',
                            color: '#141414'
                        }}
                        >
                            &times;
                        </a>
                    </div>
                </section>
        </div>

    )

}