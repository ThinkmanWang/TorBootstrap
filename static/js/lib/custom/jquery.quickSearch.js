
/*
基礎的快速搜索框插件
需要jQuery, 以及僅能使用在metronic的部份情況
*/
(function ($, window, document, undefined) {

    $.fn.quickOptSearch = function(option){
        
        var $this   = $(this);
        var options = ( typeof option === 'object' ) ? $.extend({}, $.fn.quickOptSearch.defaults, option) : $.fn.quickOptSearch.defaults;
        //將option全部添加data-filter attribute
        var valueSource = options.valueOrigin;
        var tarEle = options.targetElement;
        $this.find(valueSource).each(function(){
            var opt_value = $(this).val();
            var opt_name;
            if (!options.useDictionary)
                {
                    opt_name  = $(this).text();
                }
            else
                {
                    if (opt_value in options.dataDictionary)
                        {
                            opt_name = options.dataDictionary[opt_value][options.dictNameColumn];
                            if ('APP_PACKETNAME' in options.dataDictionary[opt_value])
                                {
                                    opt_name+= options.dataDictionary[opt_value]['APP_PACKETNAME'];
                                }
                        }
                    else
                        {
                            opt_name = '';
                        }
                    //console.log(opt_name);
                }

                    
            var filterStr = opt_value+opt_name;
            //console.log(filterStr);
            if (tarEle === 'option')
                {
                    $(this).attr('data-filter',filterStr);
                }
            else
                {
                    $(this).parent(tarEle).attr('data-filter',filterStr);
                }
        });

        var $inputElement = $('<div class="input-group qksh"><input type="text" class="form-control" placeholder="'+options.placeholder+'"><span class="input-group-btn"><button class="btn default" type="button"><i class="fa fa-search"></i></button></span></div>');
        
        $inputElement.find('button').click(function(){
            //alert('hihi');

            var query = $inputElement.find('input').val();
            //console.log(query);
            if (query !== '')
                {
                    //利用filter做篩選
                    $this.find(tarEle).not('[data-filter*="'+query+'"]').hide();
                }
            else
                {
                    $this.find(tarEle).show();
                }
        });
        $this.parent('div').append($inputElement);

    }

    $.fn.quickOptSearch.defaults = {
        valueOrigin : 'option',
        targetElement : 'option',
        placeholder : '',
        useDictionary : false,
        dataDictionary : '',
        dictNameColumn : '',

    }

})(window.jQuery, window, document);
