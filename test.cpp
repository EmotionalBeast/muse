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