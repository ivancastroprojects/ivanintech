from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from datetime import datetime
import uuid

# Schema base para compartir atributos comunes
class NewsItemBase(BaseModel):
    title: Optional[str] = None # Hacer opcional para Update
    # source: Optional[str] = None # Campo antiguo, parece reemplazado
    url: Optional[HttpUrl] = None
    description: Optional[str] = None
    imageUrl: Optional[HttpUrl] = None
    # Nuevos campos
    relevance_score: Optional[int] = None
    # time_category: Optional[str] = None # Este campo no parece usarse ya
    sectors: Optional[List[str]] = None
    publishedAt: Optional[datetime] = None 
    # Añadir campos que faltaban y que usa el CRUD
    sourceName: Optional[str] = None 
    sourceId: Optional[str] = None 

# Schema para crear un nuevo item (requiere título y url)
class NewsItemCreate(NewsItemBase):
    title: str # Sobrescribir para que sea requerido
    url: HttpUrl # Sobrescribir para que sea requerido
    # Los demás son opcionales y vienen de Base
    # sourceName y sourceId son opcionales

# Schema para actualizar un item (todos los campos opcionales)
class NewsItemUpdate(NewsItemBase):
    pass # Hereda todos los campos opcionales de Base

# Schema para leer/retornar un item
class NewsItemRead(NewsItemBase):
    id: uuid.UUID # Cambiado de int a uuid.UUID si corresponde
    title: str # Asegurar que title no sea opcional al leer
    url: HttpUrl # Asegurar que url no sea opcional al leer
    publishedAt: datetime # Asegurar que publishedAt no sea opcional al leer
    # Los demás campos pueden ser Optional según la base
    sourceName: Optional[str] = None # Asegurar que se incluya en la lectura
    sourceId: Optional[str] = None # Asegurar que se incluya en la lectura

    class Config:
        from_attributes = True # Reemplazo de orm_mode 