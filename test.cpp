#include <QFontDatabase>
QString loadFontFromFile(QString path)
{
    static QString font;
    static bool loaded = false;
    if(!loaded)
    {
        loaded = true;
        int loadedFontID = QFontDatabase::addApplicationFont(path); 
        QStringList loadedFontFamilies = QFontDatabase::applicationFontFamilies(loadedFontID); 
        if(!loadedFontFamilies.empty()) 
            font = loadedFontFamilies.at(0);
    }
    return font;
}
QString fontName = loadFontFromFile(":/font/font2.TTC");
QFont font(fontName);




void moveRow( QTableWidget *pTable, int nFrom, int nTo )
{
    if( pTable == NULL ) return;
    pTable->setFocus();

    if( nFrom == nTo ) return;

    if( nFrom < 0 || nTo < 0 ) return;
    
    int nRowCount = pTable->rowCount();

    if( nFrom >= nRowCount  || nTo > nRowCount ) return;

    if( nTo < nFrom ) nFrom++;

    pTable->insertRow( nTo );

    int nCol = pTable->columnCount();

    for( int i=0; i<nCol; i++ ) {
        pTable->setItem( nTo, i, pTable->takeItem( nFrom , i ) );
    }
    if( nFrom < nTo  ) nTo--;
    pTable->removeRow( nFrom );
    pTable->selectRow( nTo );
}

int nRow = ui->tableWidget->currentRow();

// 上移一行
 moveRow( ui->tableWidget, nRow, nRow-1 );

//下移一行
moveRow( ui->tableWidge, nRow, nRow+2 );





///注册事件过滤器
ui.tableWidget->viewport()->installEventFilter(this);
////拖放使能
ui.tableWidget->setDragDropMode(QAbstractItemView::DragDrop);
ui.tableWidget->setDragEnabled(true);
ui.tableWidget->setAcceptDrops(true);
ui.tableWidget->setSelectionBehavior(QAbstractItemView::SelectRows);        //以行为单位
ui.tableWidget->setEditTriggers(QAbstractItemView::NoEditTriggers);        //不能编辑行内容



 bool MITSVIRouteConfig::eventFilter(QObject *obj, QEvent *eve)
    {
    if(obj == ui.tableWidget->viewport())
    {
        if(eve->type() == QEvent::Drop)
        {
            const QMimeData *mime = ((QDropEvent*)eve)->mimeData();                    
            QByteArray encodedata = mime->data("application/x-qabstractitemmodeldatalist");
            if (encodedata.isEmpty())
            {  
                return false;  
            }  
            QDataStream stream(&encodedata, QIODevice::ReadOnly);
            while (!stream.atEnd())
            {
                int row, col;
                QMap<int,  QVariant> roleDataMap;
                ///拖的row和col
                stream >> row >> col >> roleDataMap;
                QTableWidgetItem* pDropItem = ui.tableWidget->itemAt(((QDropEvent*)eve)->pos());
                if(!pDropItem)    
                {
                    return true;
                }
                
                //放的row
                if(pDropItem->row() == row)
                {
                    return true;
                }
                
                ///自己的实现TODO:
 
        
                return true;    //不要交给系统处理，否则他会给你新增一行
            }
        }else
        {
            return QWidget::eventFilter(obj,eve);
        }
    }
    return QWidget::eventFilter(obj,eve);
}