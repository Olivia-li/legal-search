<script>
  export default {
    data() {
      return {
        rawHtml: "<h1><span>This</span> is an <span>example</span> Document</h1><br><p><span>This</span> is a <span>definition</span> we <span>want</span> to <span>hit</span></p>",
        definitions: {'definition': "An example Definition for what you wanna get out this.", 
        'example': 'An example is an example of another thing.', 
        'hit': 'To strike, land on, etc.',
        'want': 'To desire, long for, etc.',
        'This': 'Referring to a self.'},
        displayList: [],
        id: 1
      }
    },
    methods: {
      searchDefinitions(event) {
        const clickedWord = event.srcElement.innerText;
        if(!this.definitions[clickedWord]) return;

        if(this.displayList.find(entry => entry['word'] == clickedWord)) {
          this.displayList.sort((a, b) => (a['word'] === clickedWord && -1) || (b['word'] === clickedWord && 1) || 0)
        } else {
          this.displayList.unshift({'id': this.id, 'word': clickedWord, 'answer': this.definitions[clickedWord]})
          this.id++
        }
      }
    }
  }
</script>

<template>
<div class="flex h-screen">
  <div class="w-3/4 bg-gray-100">
    <div class="flex justify-center pt-12">
      <span v-html="rawHtml" @click="searchDefinitions"></span>
    </div>
  </div>
  <div class="w-1/4 border border-l-2 border-slate-700 overflow-y-auto">
    <ol class="py-4 space-y-2 px-2 divide-y-2 divide-blue-200">
      <li v-for="hash in displayList" :key="hash.id" class="flex flex-col pt-4">
        <p class="font-semibold">{{ hash.id }}. {{ hash['word'] }}</p>
        <p>{{ hash['answer'] }}</p>
      </li>
    </ol>
  </div>
</div>
</template>