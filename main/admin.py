from django.contrib import admin
import nested_admin
from .models import Profile, Chapter, Lesson, PointTable, Block, DivBlock, TwoTable, TwoTableData, FourTable, FourTableData, Example, MoreInfo, Practice, Sentence, Vocabulary, GrammarNote, InfoLink, Flashcard, FlashcardSet, BetaEmail

class FourTableDataInline(nested_admin.NestedTabularInline):
    model = FourTableData
    exclude = ('f_prea', 'f_preb', 'f_prec', 'f_posta', 'f_postb', 'f_postc')
    extra = 1

class FourTableInline(nested_admin.NestedTabularInline):
    model = FourTable
    inlines = [FourTableDataInline]
    extra = 1

class TwoTableDataInline(nested_admin.NestedTabularInline):
    model = TwoTableData
    exclude = ('f_prea', 'f_posta', 'f_note',)
    extra = 1

class TwoTableInline(nested_admin.NestedTabularInline):
    model = TwoTable
    inlines = [TwoTableDataInline]
    extra = 1

class ExampleInline(nested_admin.NestedTabularInline):
    model = Example
    # exclude = ('f_english', 'f_hiragana', 'f_kanji',)
    extra = 1

class MoreInfoInline(nested_admin.NestedTabularInline):
    model = MoreInfo
    extra = 1

class InfoLinkInline(nested_admin.NestedTabularInline):
    model = InfoLink
    extra = 1

class DivBlockInline(nested_admin.NestedTabularInline):
    model = DivBlock
    exclude = ('f_text',)
    extra = 1

class BlockInline(nested_admin.NestedTabularInline):
    model = Block
    exclude = ('f_text',)
    extra = 1

class PointTableInline(nested_admin.NestedTabularInline):
    model = PointTable
    exclude = ('f_pointa', 'f_pointb')
    extra = 1

class LessonAdmin(nested_admin.NestedModelAdmin):
    list_display = ('title', 'overview', 'chapter')
    # exclude = ('f_english', 'f_hiragana', 'f_kanji',)
    inlines = [PointTableInline, BlockInline, DivBlockInline, TwoTableInline, FourTableInline, ExampleInline, MoreInfoInline, InfoLinkInline]
    search_fields = ['title', 'english', 'hiragana']

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'status')

class VocabularyAdmin(nested_admin.NestedModelAdmin):
    list_display = ('english', 'kana', 'kanji', 'partofspeech', 'chapter')
    list_filter = ('chapter',)
    search_fields = ['english', 'kana', 'kanji']

class PracticeAdmin(admin.ModelAdmin):
    list_display = ('pone_english', 'pone_literal', 'pone_kana_all', 'ptwo_english', 'ptwo_literal', 'ptwo_kana_all', 'vieworder', 'strict')
    list_filter = ('lesson',)
    ordering = ('vieworder',)
    search_fields = ['pone_english', 'ptwo_english', 'pone_kana', 'ptwo_kana', 'pone_kanji', 'ptwo_kanji', 'pone_literal', 'ptwo_literal', 'pone_context', 'ptwo_context']

class SentenceAdmin(admin.ModelAdmin):
    list_display = ('english', 'literal', 'context', 'strict')
    list_filter = ('lesson',)
    search_fields = ['english', 'kana', 'kanji', 'context', 'literal']

class GrammarNoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson')

class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('user', 'english', 'kana')

class FlashcardSetAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'name')

admin.site.register(BetaEmail)
admin.site.register(GrammarNote, GrammarNoteAdmin)
admin.site.register(Sentence, SentenceAdmin)
admin.site.register(Practice, PracticeAdmin)
admin.site.register(Vocabulary, VocabularyAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Profile)
admin.site.register(Flashcard, FlashcardAdmin)
admin.site.register(FlashcardSet, FlashcardSetAdmin)
