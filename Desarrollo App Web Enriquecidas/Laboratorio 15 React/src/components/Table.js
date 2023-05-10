import Button from './Button.js';
import React, {Component} from 'react';

import Moment from 'react-moment';
import 'moment-timezone';
import 'moment/locale/es';

const Table = ({list,onDismiss}) => 
    <div className="table">
        {list. map(item => {
                return <div key={item.objectID} className="table-row">
                    <span style={{width: '40%'}}><a href={item.url}>{item.title}</a></span>
                    <span style={{width: '20%'}}>{item.author}</span>
                    
                    <span style={{width: '10%'}}><Moment locale="es" fromNow>{item.created_at}</Moment></span>
                    
                    <span style={{width: '10%'}}>{item.num_comments}</span>
                    
                    <span style={{width: '10%'}}>{item.points}</span>
                    <span style={{width: '10%'}}>
                        <Button className="button-inline" onClick={() => onDismiss(item.objectID)}>Dismiss</Button>
                    </span>
                    
                </div>

            })}
            </div>

export default Table;